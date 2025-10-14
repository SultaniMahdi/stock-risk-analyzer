import yfinance as yf
import pandas as pd

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
    data = yf.download(ticker, start=start, end=end)
    if data.empty:
        raise ValueError(f"No data found for {ticker}")
    data["returns"] = data["Adj Close"].pct_change()
    return data.dropna()
