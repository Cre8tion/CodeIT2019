import logging
import json
import re

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/encryption', methods=['POST'])
def secret():
	data = request.get_json()
	arr = []
	pattern = re.compile('[\W_]+')
	for i in range(len(data)):
		jump = data[i]["n"]
		text = data[i]["text"]
		print("txt: {}".format(text))
		newTxt = pattern.sub('', text)
		newTxt = newTxt.upper()
		print("newTxt: {}".format(newTxt))
		idx = 0
		txtIdx = 0
		ans = [None] * len(newTxt)
		length = len(newTxt)
		while None in ans:
			if idx > length:
				idx = ans.index(None)
				ans[idx] = newTxt[txtIdx]
			else:
				ans[idx] = newTxt[txtIdx]
			idx += jump
			txtIdx += 1
		joined = "".join(ans)
		print("joined: {}".format(str(joined)))
		arr.append(str(joined))
	
	print("answer: {}".format(arr))
	return json.dumps(arr)