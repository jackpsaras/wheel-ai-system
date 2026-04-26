from sheets import connect
from analyzer import analyze_stock
from put_engine import find_put
from call_engine import find_call
from close_engine import check_close_opportunity
from discord_alerts import send
import config
import time

def run():

    client = connect()
    sheet = client.open(config.SHEET_NAME)

    config_ws = sheet.worksheet("CONFIG")
    pos_ws = sheet.worksheet("POSITIONS")
    watch_ws = sheet.worksheet("WATCHLIST OUTPUT")
    trades_ws = sheet.worksheet("TRADES")

    tickers = [r["Ticker"] for r in config_ws.get_all_records() if str(r["Active"]).upper() == "TRUE"]
    positions = {r["Ticker"]: r for r in pos_ws.get_all_records()}
    trades = trades_ws.get_all_records()

    rows = []

    # 📊 DAILY SUMMARY COUNTERS
    sell_put_count = 0
    sell_call_count = 0
    close_count = 0

    # 📦 COUNT OPEN POSITIONS
    open_positions = sum(1 for p in positions.values() if int(p["Shares"]) >= 100)

    # 🔁 MAIN LOOP (SCAN TICKERS)
    for t in tickers:

        try:
            price, change, rsi, signal = analyze_stock(t, config.SETTINGS)
        except Exception as e:
            print(f"Error analyzing {t}: {e}")
            continue

        put_data = None
        call_data = None

        pos = positions.get(t, {"Shares": 0, "Cost Basis": 0})

        # 🟢 SELL PUT LOGIC
        if pos["Shares"] == 0 and signal == "SELL PUT":

            put_data = find_put(
                t,
                price,
                target_delta=config.SETTINGS["target_delta"],
                min_dte=config.SETTINGS["min_dte"],
                max_dte=config.SETTINGS["max_dte"]
            )

            if put_data:
                sell_put_count += 1

                send(config.DISCORD_WEBHOOK, f"""
🚨 SELL PUT ALERT 🚨

Ticker: {t}
Strike: {put_data[0]}
Expiry: {put_data[1]}
Premium: {put_data[2]}
Delta: {round(put_data[3], 2)}
""")

        # 🔵 SELL COVERED CALL LOGIC
        if int(pos["Shares"]) >= 100:

            call_data = find_call(
                t,
                price,
                float(pos["Cost Basis"]),
                target_delta=config.SETTINGS["call_delta"],
                min_dte=config.SETTINGS["min_dte"],
                max_dte=config.SETTINGS["max_dte"]
            )

            if call_data:
                sell_call_count += 1

                send(config.DISCORD_WEBHOOK, f"""
🔵 SELL COVERED CALL 🔵

Ticker: {t}
Strike: {call_data[0]}
Expiry: {call_data[1]}
Premium: {call_data[2]}
Delta: {round(call_data[3], 2)}
""")

        rows.append([
            t,
            price,
            change,
            rsi,
            signal,
            put_data[0] if put_data else "",
            put_data[1] if put_data else "",
            call_data[0] if call_data else "",
            call_data[1] if call_data else "",
            (put_data[2] if put_data else call_data[2] if call_data else ""),
            time.strftime("%Y-%m-%d %H:%M:%S")
        ])

    # 💰 CLOSE EARLY ENGINE
    for trade in trades:

        if trade["Status"] != "OPEN":
            continue

        try:
            result = check_close_opportunity(trade)
        except Exception as e:
            print(f"Error checking trade {trade}: {e}")
            continue

        if not result:
            continue

        current_price, profit_pct = result

        if profit_pct >= 0.5:
            close_count += 1

            send(config.DISCORD_WEBHOOK, f"""
💰 CLOSE TRADE ALERT 💰

Ticker: {trade['Ticker']}
Type: {trade['Type']}
Strike: {trade['Strike']}
Expiry: {trade['Expiry']}

Entry Premium: {trade['Entry Premium']}
Current Price: {round(current_price, 2)}

Profit: {round(profit_pct * 100, 1)}%

👉 Close this position
""")

    # 📊 UPDATE SHEET
    watch_ws.update(values=rows, range_name=f"A2:K{len(rows)+1}")

    # 📱 DAILY SUMMARY ALERT
    send(config.DISCORD_WEBHOOK, f"""
📊 **Daily Wheel Summary**

🔎 Tickers Scanned: {len(tickers)}

🟢 Sell Put Signals: {sell_put_count}
🔵 Sell Call Signals: {sell_call_count}
💰 Close Alerts: {close_count}

📦 Open Positions: {open_positions}
""")

run()