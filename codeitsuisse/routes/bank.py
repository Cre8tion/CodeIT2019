import json, logging, math, functools

from flask import request, jsonify, Response
from codeitsuisse import app

@app.route('/bankbranch', methods=['POST'])
def bank():
    data = request.get_json()
    logging.info("full data {}".format(data))

    n = data['N']
    banks = data['branch_officers_timings']
    lcm = banks[0]
    servedPerRound = []
    
    for i in banks[1:]:
        lcm = lcm*i/math.gcd(lcm, i)
    for j in banks:
        servedPerRound.append(lcm // banks)
    
    totalPerRound = functools.reduce(lambda x, y: x + y, servedPerRound)
    reduced = n % totalPerRound

    result = {}
    if reduced == 0:
        result["answer"] = 1
    else:
        

    print(result)
    return Response(json.dumps(result), mimetype='application/json')