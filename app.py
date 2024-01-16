import json
import logging

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
    data = request.json
    app.logger.debug(f"data: {data}")
    app.logger.debug(f"request.mimetype: {request.mimetype}")
    descriptions = [record["itemdesc"] for record in data["instances"]]
    results = [
        {"description": f"auto-generated-desc-for-{desc}"}
        for desc in descriptions
    ]
    return flask.Response(
        json.dumps(results),
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
