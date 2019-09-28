import json, logging

from flask import request, jsonify, Response
from codeitsuisse import app

@app.route('/exponent', methods=['POST'])
def exponent():
    data = request.get_json()
    n = data['n']
    p = data['p']

    exp = str(n ** p)
    logging.info("val " + exp)
    fd = int(exp[0])
    length = len(str(exp))
    ld = int(exp[-1])

    lst = [fd, length, ld]
    result = {"result" : lst}
    return Response(json.dumps(result), mimetype='application/json')
           