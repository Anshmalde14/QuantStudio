import os
import yfinance as yf
import pandas as pd
from config import RAW_DATA_PATH

class MarketDataLoader:
    def __init__(self):
        os.makedirs(RAW_DATA_PATH, exist_ok=True)
    def download_data(
        self,
        ticker,
        start_date="2015-01-01",
        end_date=None,
        force_download=False
    ):
        file_path = os.path.join(RAW_DATA_PATH, f"{ticker}.csv")
        if os.path.exists(file_path) and not force_download:
            print(f"Loading cached data for {ticker}")
            return pd.read_csv(file_path, parse_dates=["Date"])
        print(f"Downloading {ticker}...")
        df = yf.download(
            ticker,
            start=start_date,
            end=end_date,
            progress=False,
            auto_adjust=False
        )
        df.reset_index(inplace=True)
        # Flatten MultiIndex columns
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [col[0] for col in df.columns]
        df["Asset"] = ticker
        df.to_csv(file_path, index=False)
        return df