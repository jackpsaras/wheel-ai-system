🚀 Wheel AI Trading System






An automated options trading assistant that helps you execute the wheel strategy with discipline, consistency, and real-time alerts.

🧠 Overview

This project is a Python-based system that:

Scans stocks daily
Identifies high-probability options trades
Sends real-time alerts
Tracks performance automatically

It combines data analysis + automation + structured rules to remove emotion from trading.

⚙️ Core Features
🟢 Automated Trade Signals
Detects opportunities to sell cash-secured puts
Suggests covered calls when shares are owned
Uses delta targeting for consistent risk management
💰 Close Early Profit Alerts
Monitors open trades
Alerts when 50–70% profit is reached
Helps lock gains and redeploy capital faster
📊 Daily Summary Notifications
Sends a clean summary to Discord
Includes:
Signals generated
Open positions
Close alerts
📋 Google Sheets Integration
Tracks:
Watchlist
Positions
Trades
Automatically updates:
Prices
RSI
Signals
🎯 Custom Strategy Settings

Fully customizable:

RSI Threshold
Dip Percentage
Delta Targets
Days to Expiration
🔄 How It Works
1. Pull market data (yfinance)
2. Analyze tickers (RSI + dip logic)
3. Generate signals (PUT / CALL)
4. Check open trades for exits
5. Update Google Sheets
6. Send Discord alerts
🧰 Tech Stack
Python
yfinance
pandas
gspread
Google Sheets API
Discord Webhooks
📁 Project Structure
wheel-ai-system/
│
├── main.py                # Orchestrates system
├── analyzer.py            # Entry signal logic
├── put_engine.py          # Put selection logic
├── call_engine.py         # Covered call logic
├── close_engine.py        # Close early logic
├── sheets.py              # Google Sheets connection
├── discord_alerts.py      # Discord alerts
├── config.py              # Strategy settings
└── creds.json             # Google API credentials
🔔 Example Alerts
🚨 Sell Put Alert
Ticker: AAPL
Strike: 180
Expiry: 2026-05-01
Premium: 2.10
💰 Close Trade Alert
Ticker: NVDA
Profit: 63%
Action: Close position
📊 Daily Summary
Tickers Scanned: 5
Sell Put Signals: 2
Sell Call Signals: 1
Close Alerts: 1
Open Positions: 3
🚀 Getting Started
1. Clone the repo
git clone https://github.com/yourusername/wheel-ai-system.git
cd wheel-ai-system
2. Install dependencies
pip install -r requirements.txt
3. Set up Google Sheets API
Create a service account
Download creds.json
Share your sheet with the service account email
4. Configure your sheet

Create tabs:

CONFIG
POSITIONS
WATCHLIST OUTPUT
TRADES
5. Add Discord webhook

In config.py:

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/..."
6. Run the system
python main.py
📈 Strategy Settings (Default)
Setting	Value
RSI Threshold	45
Dip Threshold	-2%
Target Delta	0.25
Call Delta	0.25
Min DTE	7
Max DTE	14
⚠️ Disclaimer

This project is for educational purposes only and does not constitute financial advice.

Options trading involves risk and may not be suitable for all investors.

🔮 Future Improvements
📊 Position sizing engine
🌐 Web dashboard (SaaS)
🤖 Trade optimization engine
📉 Backtesting system
👥 Multi-user support
⭐ Contributing

Pull requests are welcome. For major changes, please open an issue first.

📬 Contact

Built as a structured approach to systematic options trading.

If you find this useful, consider starring the repo ⭐