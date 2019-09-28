import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/generateSequence', methods=['POST'])
def seq():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    

    nodes = data["modules"]
    edges = {}

    for d in data["dependencyPairs"]:
        start = d['dependentOn']
        end = d['dependee']
        if start in edges:
            edges[start] = edges[start].append(end)
        else:
            edges[start] = [end]

    logging.info("nodes {}".format(nodes))
    logging.info("edges {}".format(edges))
    

    return json.dumps([])