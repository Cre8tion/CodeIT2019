import logging
import json
import re

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/encryption', methods=['POST'])
def secret():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    arr = []

    pattern = re.compile('([^\w]|_)+')

    for i in range(len(data)):
    	jump = data[i]["n"] - 1
    	text = data[i]["text"]
    	newtxt = pattern.sub('', text)
    	newtxt = newtxt.upper()
    	lst = list(newtxt)
    	idx = 0
    	ans = []
    	while(idx + jump < len(lst)):
    		ans[idx] = lst[idx]
    		idx = idx + jump

    	

    result = "s"
    logging.info("My result :{}".format(result))
    return json.dumps(result)