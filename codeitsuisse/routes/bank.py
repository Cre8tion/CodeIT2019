import json, logging, math, functools
from math import gcd

from flask import request, jsonify, Response
from codeitsuisse import app

@app.route('/bankbranch', methods=['POST'])
def bank():
    data = request.get_json()
    logging.info("full data {}".format(data))

    n = data['N']
    banks = data['branch_officers_timings']
    Lcm = banks[0]
    for i in range(1,len(banks)):
        Lcm = getLCM(Lcm,banks[i])
    remainder = n % Lcm
    if(remainder < len(banks)):
        answer = remainder + 1
    else:
        answer = 0
    
        

    result = {"answer":answer}
    return Response(json.dumps(result), mimetype='application/json')

def getLCM(a, b):
    return a * b // gcd(a, b)