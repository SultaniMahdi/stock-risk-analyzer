import pytest
from src.data_fetcher import fetch_data


def test_fetch_data_returns_dataframe():
    data = fetch_data("AAPL")
    assert "returns" in data.columns, "Data should contain a 'returns' column"
    assert len(data) > 0, "Fetched data should not be empty"
