import json
import logging
import random
from typing import List, Dict, Union

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
    record = request.json
    app.logger.debug(f"data: {record}")
    app.logger.debug(f"request.mimetype: {request.mimetype}")
    itemdesc = record["features"][0]
    app.logger.debug(f"Calling with: {itemdesc}")
    result = json.dumps({
        "itemdesc": itemdesc,
        "predictions": _get_prediction(itemdesc),
    })
    app.logger.debug(f"Result: {result}")
    return flask.Response(result, mimetype='application/jsonlines')


def _get_prediction(item_description: str) -> List[Dict[str, Union[str, int]]]:
    return [
        {
            f"prediction-{i}": f"auto-generated-description-for-{item_description}-{i}",
            f"probability-{i}": random.random(),
        }
        for i in range(3)
    ]


if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
