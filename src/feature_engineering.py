import numpy as np
import pandas as pd

class FeatureEngineer:

    def __init__(self):
        pass

    def add_price_features(self, df):
        df = df.copy()
        df["Daily_Return"] = df["Close"].pct_change()
        df["Log_Return"] = np.log(df["Close"] / df["Close"].shift(1))
        df["Return_Lag_1"] = df["Daily_Return"].shift(1)
        df["Return_Lag_5"] = df["Daily_Return"].shift(5)
        df["Rolling_STD_20"] = df["Close"].rolling(20).std()
        df["Rolling_STD_10"] = df["Close"].rolling(10).std()
        df["Intraday_Range"] = (df["High"] - df["Low"]) / df["Close"]
        return df

    def add_trend_features(self, df):
        df = df.copy()
        # simple moving average
        df["SMA_10"] = df["Close"].rolling(10).mean()
        df["SMA_20"] = df["Close"].rolling(20).mean()

        # exponential moving average
        df["EMA_10"] = df["Close"].ewm(span=10,adjust = False).mean()
        df["EMA_20"] = df["Close"].ewm(span=20,adjust = False).mean()
        df["EMA_12"] = df["Close"].ewm(span=12,adjust = False).mean()
        df["EMA_26"] = df["Close"].ewm(span=26,adjust = False).mean()
        df["MACD"] = df["EMA_12"] - df["EMA_26"]
        df["MACD_Signal"] = df["MACD"].ewm(span=9,adjust = False).mean()
        return df

    def add_momentum_features(self, df):
        df = df.copy()
        # relative strength Index(RSI)
        delta = df["Close"].diff()
        gain = delta.clip(lower = 0)
        loss = -delta.clip(upper = 0)
        avg_gain = gain.rolling(14).mean()
        avg_loss = loss.rolling(14).mean()
        rs = avg_gain/avg_loss
        df["RSI_14"] = 100 - (100 / (1 + rs))

         #ROC :- Rate of Change
        df["ROC_10"] = ((df["Close"] - df["Close"].shift(10)) / df["Close"].shift(10)) * 100
        
        #Momentum
        df["Momentum_10"] = df["Close"] - df["Close"].shift(10)
        return df
    def add_volatility_features(self, df):
        df = df.copy()
        #Bollinger Band
        df["BB_Middle"] = df["Close"].rolling(20).mean()
        rolling_std = df["Close"].rolling(20).std()
        df["BB_Upper"] = df["BB_Middle"] + (rolling_std * 2)
        df["BB_Lower"] = df["BB_Middle"] - (rolling_std * 2)

        #Average True Range(ATR)
        high_low = df["High"] - df["Low"]
        high_close = (df["High"] - df["Close"].shift(1)).abs()
        low_close = (df["Low"] - df["Close"].shift(1)).abs()
        true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        df["ATR_14"] = true_range.rolling(14).mean()

        #Historical Volatility
        df["Historical_Volatility_20"] = (df["Daily_Return"].rolling(20).std())*np.sqrt(252)
        return df

    def generate_features(self, df):
            df = self.add_price_features(df)
            df = self.add_trend_features(df)
            df = self.add_momentum_features(df)
            df = self.add_volatility_features(df)
            return df