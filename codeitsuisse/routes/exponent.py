import json, logging, math

from flask import request, jsonify, Response
from codeitsuisse import app

@app.route('/exponent', methods=['POST'])
def exponent():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    n = data['n']
    p = data['p']

    if(n == 0):
        fd = 0
        length = 1
        ldigit = 0
    elif(n == 10):
        fd = 1
        length = p + 1
        ldigit = 0
    elif(p == 0):
        fd = 1
        length = 1
        ldigit = 1
    elif(n == 1):
        fd = 1
        length = 1
        ldigit = 1
    else:
        length = p * math.log10(n)
        frac, whole = math.modf(length)
        fd = int(str(10 ** frac)[0])
        print(fd)
        length = int(math.ceil(length))
        print(length)

        num = str(n)
        ld = int(num[len(num)-1])

        if(ld == 1):
            ldigit = 1
        elif(ld == 2):
            remainder = p % 4
            arr = [2,4,8,6]
            ldigit = arr[remainder - 1]
        elif(ld == 3):
            remainder = p % 4
            arr = [3,9,7,1]
            ldigit = arr[remainder - 1]
        elif(ld == 4):
            remainder = p % 4
            arr = [4,6,4,6]
            ldigit = arr[remainder - 1]
        elif(ld == 5):
            ldigit = 5
        elif(ld == 6):
            ldigit = 6
        elif(ld == 7):
            remainder = p % 4
            arr = [7,9,3,1]
            ldigit = arr[remainder - 1]
        elif(ld == 8):
            remainder = p % 4
            arr = [8,4,2,6]
            ldigit = arr[remainder - 1]
        elif(ld == 9):
            remainder = p % 4
            arr = [9,1,9,1]
            ldigit = arr[remainder - 1]
        elif(ld == 0):
            ldigit = 0
        #res = ld**p
        #ldigit = int(res % 10)
        print(ldigit) 

    lst = [fd, length, ldigit]
    result = {"result" : lst}
    logging.info("My result :{}".format(result))
    return Response(json.dumps(result), mimetype='application/json')


def Modulo(a, b) : 
    mod = 0
  
    # calculating mod of b with a to make 
    # b like 0 <= b < a 
    for i in range(0, len(b)) : 
        mod = (mod * 10 + (int)(b[i])) % a 
  
    return mod # return modulo 
           