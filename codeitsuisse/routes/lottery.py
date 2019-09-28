import json, logging
from random import randint
from flask import request, jsonify
from codeitsuisse import app

@app.route('/lottery', methods=['GET'])
def lottery():
    lst = []
    for i in range(10):
        lst.append(str(randint(1,100)))

    
    logging.info("rand nums {}".format(lst))
    return json.dumps(lst)