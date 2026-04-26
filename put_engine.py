import yfinance as yf
import numpy as np
from scipy.stats import norm
from datetime import datetime

def calc_delta(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    return norm.cdf(d1)

def find_put(ticker, price, target_delta, min_dte, max_dte):

    stock = yf.Ticker(ticker)

    best = None
    best_diff = 999

    for exp in stock.options:
        dte = (datetime.strptime(exp, "%Y-%m-%d") - datetime.today()).days

        if dte < min_dte or dte > max_dte:
            continue

        chain = stock.option_chain(exp)

        for _, row in chain.puts.iterrows():
            K = row["strike"]
            iv = row["impliedVolatility"]

            if iv <= 0:
                continue

            delta = calc_delta(price, K, dte/365, 0.01, iv)

            diff = abs(delta - target_delta)

            if diff < best_diff:
                best_diff = diff
                best = (K, exp, row["lastPrice"], delta)

    return best