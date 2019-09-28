import json, logging
from random import randint
from flask import request, jsonify
from codeitsuisse import app

@app.route('/lottery', methods=['POST'])
def lottery():
    lst = []
    for i in range(10):
        lst.append(randint(1,100))

    
    logging.info("rand nums {}".format(lst))
    return(json.dumps(lst))