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
    data = request.get_json()
    item_desc = data["itemdesc"]
    return flask.Response(
        json.dumps({"category": f"predicted {item_desc}"}),
        mimetype='application/jsonlines'
    )


if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
