import yfinance as yf

def check_close_opportunity(trade):

    ticker = trade["Ticker"]
    strike = float(trade["Strike"])
    expiry = trade["Expiry"]
    entry_premium = float(trade["Entry Premium"])

    stock = yf.Ticker(ticker)
    chain = stock.option_chain(expiry)

    if trade["Type"] == "PUT":
        options = chain.puts
    else:
        options = chain.calls

    match = options[options["strike"] == strike]

    if match.empty:
        return None

    current_price = float(match.iloc[0]["lastPrice"])

    profit_pct = (entry_premium - current_price) / entry_premium

    return current_price, profit_pct