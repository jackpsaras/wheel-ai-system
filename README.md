Wheel AI Trading System

An automated options trading assistant that helps you execute the wheel strategy with discipline, consistency, and real-time alerts.

Overview

This project is a Python-based system that scans stocks daily and generates actionable options trading signals. It identifies when to sell cash secured puts, when to sell covered calls, and when to close positions early to lock in profits.

The system integrates with Google Sheets for tracking and Discord for real-time alerts, creating a lightweight but powerful trading workflow.

Core Features
Automated Trade Signals
Detects high probability opportunities to sell puts using RSI and price dip conditions
Suggests covered calls when shares are held
Uses delta targeting for consistent risk management
Close Early Profit Alerts
Monitors open trades
Sends alerts when 50–70 percent of max profit is captured
Helps reduce risk and redeploy capital faster
Daily Summary Notifications
Sends a clean daily overview to Discord
Includes number of signals, open positions, and close alerts
Google Sheets Integration
Tracks watchlist, positions, and trades
Automatically updates pricing, signals, and timestamps
Customizable Strategy Settings
RSI threshold
Dip percentage
Delta targets
Days to expiration
How It Works
Pulls market data using yfinance
Analyzes each ticker based on defined strategy rules
Generates trade signals (sell put or sell call)
Checks existing trades for early close opportunities
Updates Google Sheets with results
Sends alerts to Discord
Tech Stack
Python
yfinance
pandas
gspread
Google Sheets API
Discord Webhooks
Project Structure
wheel-ai-system/
│
├── main.py                # Orchestrates entire system
├── analyzer.py            # Entry signal logic
├── put_engine.py          # Put strike selection
├── call_engine.py         # Covered call logic
├── close_engine.py        # Close early logic
├── sheets.py              # Google Sheets connection
├── discord_alerts.py      # Discord notifications
├── config.py              # Strategy settings
└── creds.json             # Google API credentials
Example Alerts

SELL PUT ALERT
Ticker AAPL
Strike 180
Expiry 2026-05-01
Premium 2.10

CLOSE TRADE ALERT
Ticker NVDA
Profit 63 percent
Close this position

DAILY SUMMARY
Tickers Scanned 5
Sell Put Signals 2
Sell Call Signals 1
Close Alerts 1

Getting Started
Clone the repository
Install dependencies
Set up Google Sheets API credentials
Connect your sheet and configure tabs
Add your Discord webhook
Run the system daily
Disclaimer

This project is for educational purposes only and does not constitute financial advice. Trading options involves risk and may not be suitable for all investors.