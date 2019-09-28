import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/composition', methods=['POST'])
def compose():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    global patterns
    _id = data.get("setId")
    string = data.get("composition")
    patterns = data.get("patterns")
    length = len(patterns)

    for i in range(length):
    	patterns.append(patterns[i][1]+patterns[i][0])

    val = split(string,0)

    res = {"testId":f"{_id}","result":f"{val}"}
    logging.info("My result :{}".format(res))
    return json.dumps(res)


def split(str,count):
	arr = []
	count += 1
	print(str)
	for i in range(len(str)):
		s = str[0:i] + str[i+1:len(str)]
		if (any(ele in s for ele in patterns)) == False:
			print(s)
			return count
		arr.append(s)
	print(arr)
	for i in arr:
		return split(i,count)