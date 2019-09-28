import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/chessgame', methods=['POST'])
def chess():
    board = request.get_json()
    logging.info("data sent for evaluation {}".format(board))

    nrow = len(board)
    ncol = len(board[0])
    squares = 0

    for i in range(nrow):
        for j in range(ncol):
            if "K" in board[i][j]:
                queen = [i, j]

    def direction(i: int, j: int):
        nonlocal squares 
        stepRow = queen[0]
        stepCol = queen[1]
        while True:
            stepRow = stepRow + i
            stepCol = stepCol + j
            if stepRow >= 0 and stepRow < nrow and stepCol >= 0 and stepCol < ncol:
                break
            if board[stepRow][stepCol] == "X":
                break
            squares += 1
    
    direction(-1, 0)
    direction(-1, -1)
    direction(0, -1)
    direction(1, -1)
    direction(1, 0)
    direction(1, 1)
    direction(0, 1)
    direction(-1, 1)
    
    #inputValue = data.get("input");
    #result = inputValue * inputValue
    logging.info("My result :{}".format(squares))



    return json.dumps(squares)

