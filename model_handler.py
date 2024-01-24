import json
import logging
import random
from typing import List


def _get_prediction(features: List[str]) -> str:
    item_description = features[0]
    return f"auto-generated-description-for-{item_description}"


def handle(data, context):
    logging.info(f"data: {data}")
    logging.info(f"context: {context}")
    if data is None:  # first called during init, without the payload 'data'
        return None
    records = data[0]["body"]
    data = json.loads(records.decode("utf-8"))
    logging.info(f"data: {data}")

    features = data["features"]
    results = [
        {
            "predictions": _get_prediction(features),
            "probabilities": random.random()
        }
    ]
    logging.info(f"results: {json.dumps(results)}")
    return results
