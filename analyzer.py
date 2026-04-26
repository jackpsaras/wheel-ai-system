import yfinance as yf
from ta.momentum import RSIIndicator

def analyze_stock(ticker, settings):

    data = yf.download(ticker, period="3mo", interval="1d")

    if data.empty:
        return None, None, None, "WAIT"

    close = data["Close"]

    # 🔑 FIX: handle Series vs DataFrame
    if hasattr(close, "columns"):  # means it's a DataFrame
        close = close.iloc[:, 0]

    if len(close) < 2:
        return None, None, None, "WAIT"

    price = float(close.iloc[-1])
    prev_price = float(close.iloc[-2])

    change = (price - prev_price) / prev_price

    rsi = RSIIndicator(close).rsi().iloc[-1]

    signal = "SELL PUT" if change < settings["dip_threshold"] and rsi < settings["rsi_threshold"] else "WAIT"
    #signal = "SELL PUT"

    return price, change, rsi, signal