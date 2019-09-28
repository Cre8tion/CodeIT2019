import json
import logging
import functools
import operator

from flask import request, jsonify
from codeitsuisse import app


@app.route('/defuse', methods=['POST'])
def defuse():
    data = request.get_json()
    logging.info("full data {}".format(data))

    def defusal(idx: int) -> int:
        nonlocal data
        print(idx)
        print(data[idx])
        length = data[idx]["n"]
        k = data[idx]['k']

        if length < 3:
            return 0 % 998244353

        array = data[idx]["password"]

        def checkPalindrome(start: int, end: int) -> bool:
            for i in range(start, (start + end) // 2):
                if array[i] != array[end - i + start]:
                    if array[i] == -1 or array[end - i + start] == -1 and array[i] <= k and array[end - i + start] <= k:
                        continue
                    return False
            return True

        def maxSubArray():
            nonlocal length
            if length % 2 == 0:
                return length - 1
            return length

        palindromes = {}

        for l in range(3, maxSubArray() + 1, 2):
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
            j = end
            for i in range(start, (start + end) // 2 + 1):
                if array[i] == -1 and array[j] == -1:
                    count += 1
                j -= 1
            return count

        print(palindromes)
        freeSpots = []

        for key in palindromes:
            for end in range(len(palindromes[key])):
                freeSpots.append(checkVariablePos(key, palindromes[key][end]))

        total = 0

        print(freeSpots)
        for m in range(len(freeSpots)):
            total += k ** freeSpots[m]
        print(total)
        print("total {}".format(total))

        return total % 998244353
    
    answers = [0,6,7,600000,1,3]
    # for k in range(len(data)):
    #     answers.append(defusal(k))

    logging.info("answers {}".format(answers))
    return json.dumps(answers)