# import pandas as pd
import yfinance as yf


def fetch_data(ticker: str, start="2024-01-01", end="2024-12-31"):
    """
    Fetch historical stock data and calculate daily returns.

    Parameters:
        ticker (str): Stock symbol (e.g., 'AAPL')
        start (str): Start date in YYYY-MM-DD
        end (str): End date in YYYY-MM-DD

    Returns:
        pd.DataFrame: Stock data with daily returns
    """
    data = yf.download(ticker, start=start, end=end, auto_adjust=True)
    if data.empty:
        raise ValueError(f"No data found for {ticker}")
    data["returns"] = data["Close"].pct_change()
    return data.dropna()
