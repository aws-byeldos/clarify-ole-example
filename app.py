import json
import logging
import random
from typing import List

import flask
from flask import request

app = flask.Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.get("/")
def index_page():
    return {"message": "hello1"}


@app.get("/ping")
def read_ping():
    return flask.Response(
        {"message": "pong"},
        mimetype='application/jsonlines'
    )


@app.route('/invocations', methods=["POST"])
def invoke():
    records = request.json
    app.logger.debug(f"data: {records}")
    app.logger.debug(f"request.mimetype: {request.mimetype}")
    record_features = [record["features"] for record in records]
    return flask.Response(
        json.dumps([
            {
                "predictions": _get_prediction(features),
                "probabilities": random.random()
            }
            for features in record_features
        ]),
        mimetype='application/json'
    )


def _get_prediction(features: List[str]) -> str:
    item_description = features[0]
    return f"auto-generated-description-for-{item_description}"


if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
