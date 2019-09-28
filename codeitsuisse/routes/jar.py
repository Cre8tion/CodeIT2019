import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/readyplayerone', methods=['POST'])
def ready():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    num = data.get("maxChoosableInteger")
    total = data.get("desiredTotal")
    if(num == 1):
    	count = -1
    else:
	    lst = list(range(1,num+1))
	    limit = num + 1
	    turn = 0
	    if(num >= total/2 and num < total):
	        count = 3
	    elif(num > total):
	        count = 1
	    else:
		    while(len(lst) > 0 and total - lst[-1] > limit):
		    	turn+=1
		    	total = total - lst[-1]
		    	lst.pop(-1)
		    	limit = lst[-1]
		    	print(turn)
		    	print(total)
		    	print(lst)
		    if (len(lst) == 0 and total > 0):
		    	count = -1
		    else:
		    	count = turn + 2
    if(count % 2 == 0):
        count = -1
    result = {"res":count}

    logging.info("My result :{}".format(result))
    return json.dumps(result);

