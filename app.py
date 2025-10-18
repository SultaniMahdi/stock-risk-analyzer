from flask import Flask, jsonify, request
from src.data_fetcher import fetch_data
from src.risk_calculator import calculate_volatility


app = Flask(__name__)


@app.route("/volatility")
def get_volatility():
    ticker = request.args.get("ticker", "AAPL")
    data = fetch_data(ticker)
    vol = calculate_volatility(data["returns"])
    return jsonify({"ticker": ticker, "volatility": round(vol, 4)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
