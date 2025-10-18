import numpy as np

from src.risk_calculator import calculate_volatility


def test_calculate_volatility():
    returns = np.random.normal(0, 0.01, 50)
    vol = calculate_volatility(returns)
    assert vol > 0
