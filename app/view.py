from app.service import DollarService, RofexService, CmeService, BloombergService, Datetime
from flask import Flask, Response, jsonify, request


app = Flask(__name__)


@app.route("/status", methods=["GET"])
def status() -> None:
    """ Return Scrapping API status """
    return Response(
        response=f"The Scrapping API works!", status=200, mimetype="application/json"
    )


@app.route("/dollar", methods=["GET"])
def get_dollar_data_from_pages():
    """ Return 'Nacion Bank' & 'Rofex' dollar values """
    datetime = Datetime.get_time()
    bank_nacion_data = DollarService.get_nacion_bank_scraping_data()
    rofex_data = RofexService.get_rofex_scraping_data()
    return jsonify(datetime, bank_nacion_data, rofex_data)


@app.route("/cme", methods=["GET"])
def get_cme_data_from_pages():
    """ Return 'Cme' dollar values """
    datetime = Datetime.get_time()
    cme_data = CmeService.get_cme_scraping_data()
    return jsonify(datetime, cme_data)


@app.route("/bloomberg", methods=["GET"])
def get_bloomberg_data_from_pages():
    """ Return 'Bloomberg' dollar values """
    datetime = Datetime.get_time()
    bloomberg_data = BloombergService.get_bloomberg_scraping_data()
    return jsonify(datetime, bloomberg_data)


@app.errorhandler(404)
def not_found(error=None):
    """ Error handler for resources that are not covered """
    return Response(
        response=f'Resource not found: "{request.url}"', status=404, mimetype="application/json"
    )
