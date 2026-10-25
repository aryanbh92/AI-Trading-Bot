from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies import Strategy
from lumibot.traders import Trader
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
from datetime import datetime
from datetime import timedelta
from finbert_utils import estimate_sentiment


API_KEY = "PK22M2KYKYM3CIXA2CCDWRWA7Q"
API_SECRET = "Ceku5rW1qR7WtyPTkayFL6BdDx4S5gRbgE2h8PZs9ayB"
BASE_URL = "https://paper-api.alpaca.markets/v2"

ALPACA_CREDS = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True,

}

class MLTrader(Strategy):

    def initialize(self, symbol="SPY", cash_at_risk=0.5):
        self.symbol = symbol
        self.cash_at_risk = cash_at_risk
        self.sleeptime = "24H"
        self.last_trade = None

        self.api = REST(
            key_id=API_KEY,
            secret_key=API_SECRET,
            base_url=BASE_URL
        )

    def position_sizing(self):
        cash = self.get_cash()
        last_price = self.get_last_price(self.symbol)

        quantity = int(
            (cash * self.cash_at_risk) / last_price
        )

        return cash, last_price, quantity

    def get_dates(self):
        today = self.get_datetime()
        three_days_prior = today - timedelta(days=3)

        return (
            today.strftime("%Y-%m-%d"),
            three_days_prior.strftime("%Y-%m-%d")
        )

    def get_sentiment(self):
        today, three_days_prior = self.get_dates()

        news = self.api.get_news(
            symbol=self.symbol,
            start=three_days_prior,
            end=today
        )

        headlines = [
            item.__dict__["_raw"]["headline"]
            for item in news
        ]

        probability, sentiment = estimate_sentiment(headlines)

        return probability, sentiment

    def on_trading_iteration(self):

        cash, last_price, quantity = self.position_sizing()
        probability, sentiment = self.get_sentiment()

        if cash > last_price:

            if sentiment == "positive" and probability > 0.999:

                if self.last_trade == "sell":
                    self.sell_all()

                order = self.create_order(
                    self.symbol,
                    quantity,
                    "buy",
                    type="bracket",
                    take_profit_price=last_price * 1.20,
                    stop_loss_price=last_price * 0.95
                )

                self.submit_order(order)
                self.last_trade = "buy"

            elif sentiment == "negative" and probability > 0.999:

                if self.last_trade == "buy":
                    self.sell_all()

                order = self.create_order(
                    self.symbol,
                    quantity,
                    "sell",
                    type="bracket",
                    take_profit_price=last_price * 0.80,
                    stop_loss_price=last_price * 1.05
                )

                self.submit_order(order)
                self.last_trade = "sell"