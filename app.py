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
    records = request.data.decode('utf-8')
    app.logger.debug(f"data: {records}")
    app.logger.debug(f"request.mimetype: {request.mimetype}")
    record_features = [record.split(",")[0] for record in records.split("\n")]
    response = [
        f"{_get_prediction(itemdesc)},{random.random()}"
        for itemdesc in record_features
    ]
    return flask.Response(
        "\n".join(response),
        mimetype='text/csv'
    )


def _get_prediction(itemdesc: List[str]) -> str:
    return f"auto-generated-description-for-{itemdesc}"


if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
