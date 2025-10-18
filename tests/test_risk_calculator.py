import pandas as pd
import pytest

from src.risk_calculator import calculate_volatility


def test_calculate_volatility_positive():
    returns = pd.Series([0.01, -0.02, 0.015, -0.005])
    vol = calculate_volatility(returns)
    assert vol > 0, "Volatility should be positive"
