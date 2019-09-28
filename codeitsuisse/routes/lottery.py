import json, logging
from random import randint
from flask import request, jsonify, Response
from codeitsuisse import app

@app.route('/lottery', methods=['GET'])
def lottery():
    lst = []
    for i in range(10):
        lst.append(randint(1,100))

    
    logging.info("rand nums {}".format(lst))
    return Response(json.dumps(lst), mimetype='application/json')