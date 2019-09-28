import json, logging, math

from flask import request, jsonify, Response
from codeitsuisse import app

@app.route('/exponent', methods=['POST'])
def exponent():
    data = request.get_json()
    n = data['n']
    p = data['p']

    length = p * math.log10(n)
    length = int(math.ceil(length))

    num = str(n)
    first = num[0]
    val = int(first)**p
    final_num = str(val)
    fd = int(final_num[0])
    #
    #exp = str(n ** p)
    #logging.info("val " + exp)
    #
    #fd = int(exp[0])
    #length = len(str(exp))

    lst = [int(x) for x in str(num)] 

    mod = Modulo(4, lst)

    if((mod == 0)) : 
        exp_end = 4
    else :  
        exp_end = mod
  
    # Find last digit in 'a' and compute its exponent 
    res = n**exp_end
    ldigit = int(res % 10) 

    #ld = int(exp[-1])

    lst = [fd, length, ldigit]
    result = {"result" : lst}
    return Response(json.dumps(result), mimetype='application/json')


def Modulo(a, b) : 
    mod = 0
  
    # calculating mod of b with a to make 
    # b like 0 <= b < a 
    for i in range(0, len(b)) : 
        mod = (mod * 10 + (int)(b[i])) % a 
  
    return mod # return modulo 
           