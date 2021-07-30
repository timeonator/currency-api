
from flask import Flask, jsonify, make_response,Response
import requests


app = Flask(__name__)

@app.route("/")
def home():
    response = make_response(
        jsonify(
            {"message": "home"}
        ),
        200,
    )
    response.headers["Content-Type"] = "application/json"
    return response


currencyURI = 'https://freecurrencyapi.net/api/v1/rates'
@app.route("/convert/<from_currency>/<to_currency>")
def converter(from_currency,to_currency):
    rates = requests.get(currencyURI + '?'+ from_currency)
    raw = rates.json()
    r = list(raw['data'].values())[0]
    response = make_response(
        jsonify(
            {
            "from_currency": from_currency,
            "to_currency": to_currency,
            "rate": r[to_currency]
            }
        ),
        200,
    )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route("/rates")
def rate_view():
    rates = requests.get('https://freecurrencyapi.net/api/v1/rates?base_currency=USD')
    response = make_response(
        jsonify(rates.json()),
        rates.status_code,
    )
    response.headers["Content-Type"] = "application/json"
    return response        