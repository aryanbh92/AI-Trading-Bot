🚀 AI-Powered Trading Bot Using FinBERT & Alpaca

An AI-driven algorithmic trading system that analyzes financial news using FinBERT sentiment analysis and automatically executes trades through the Alpaca Trading API.

📌 Overview

This project combines Machine Learning, Natural Language Processing (NLP), and Algorithmic Trading to make automated trading decisions based on real-time financial news sentiment.

The bot:

Fetches financial news headlines
Performs sentiment analysis using FinBERT
Detects bullish and bearish signals
Applies risk management strategies
Executes trades through Alpaca API
Supports historical backtesting using Lumibot

⚡ Features
Real-time news sentiment analysis
Automated buy and sell decisions
Position sizing based on available capital
Stop-loss protection
Take-profit targets
Historical strategy backtesting
Easy integration with Alpaca Paper Trading

🛠️ Tech Stack
Python
Lumibot
FinBERT
Alpaca API
Yahoo Finance Data
NLP
Machine Learning

📊 Trading Logic
Buy Signal
Positive sentiment
Confidence score > 99.9%
Sell Signal
Negative sentiment
Confidence score > 99.9%
Risk Management
Position sizing based on available capital
Stop-loss at 5%
Take-profit at 20%

📈 Backtesting
The strategy can be backtested using historical market data provided by Yahoo Finance.

      strategy.backtest(
      YahooDataBacktesting,
      start_date,
      end_date
)

🚀 Future Improvements
Multi-stock portfolio support
RSI and MACD indicators
Streamlit dashboard
Performance analytics
Portfolio optimization
Reinforcement learning models

🎯 Key Learnings
Algorithmic Trading
Financial Data Analysis
NLP with FinBERT
Risk Management
API Integration
Backtesting Strategies
🤝 Contributions

Contributions, suggestions, and improvements are welcome.
