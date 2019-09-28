import json, logging, functools, operator

from flask import request, jsonify
from codeitsuisse import app

@app.route('/defuse', methods=['POST'])
def defuse():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    length = data['n']

    if length < 3:
        return json.dumps(0)

    array = data["password"]

    def checkPalindrome(start: int, end: int) -> bool:
        for i in range(start, (start + end) // 2):
            if array[i] != array[end - i + start]:
                return False
        return True
    
    def maxSubArray():
        nonlocal length
        if length % 2 == 0:
            return length - 1
        return length

    palindromes = {}

    for l in range (3, maxSubArray() + 1, 2): 
        for i in range(length):
            if i + l - 1 >= length:
                continue
            j = i + l - 1
            if checkPalindrome(i, j):
                if i in palindromes:
                    palindromes[i].append(j)
                else:
                    palindromes[i] = [j]

    def checkVariablePos(start: int, end: int) -> int:
        count = 0
        for i in range(start, (start + end) // 2 + 1):
            if array[i] == -1:
                count += 1
        return count
    
    print(palindromes)
    freeSpots = []
    
    logging.info("freeSpots {}".format(freeSpots))

    for key in palindromes:
        for end in range(len(palindromes[key])):
            print("key {}".format(key))
            print("end {}".format(palindromes[key][end]))
            freeSpots.append(checkVariablePos(key, palindromes[key][end]))
    
    total = 0
    k = data['k']

    print(freeSpots)
    for m in range(len(freeSpots)):
        total += k ** freeSpots[m]
    print(total)
    logging.info("total {}".format(total))

    return json.dumps(total)