import numpy as np

def calculate_volatility(returns, window=30):
    if len(returns) < window:
        raise ValueError("Not enough data points")
    return np.sqrt((returns[-window:] ** 2).mean())
