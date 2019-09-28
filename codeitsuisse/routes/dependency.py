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
    graph = {}

    for d in data["dependencyPairs"]:
        start = d['dependentOn']
        end = d['dependee']
        if start in graph:
            graph[start].add(end)
        else:
            graph[start] = set([end])

    stack = [nodes[0]]
    visited = {}

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            



    return json.dumps([])