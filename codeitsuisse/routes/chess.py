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

    row = queen[0]
    col = queen[1]

    def reset():
        nonlocal row, col
        row = queen[0]
        col = queen[1]

    def direction(i: int, j: int):
        nonlocal row, col, squares
        while row >= 0 and row < nrow and col >= 0 and col < ncol:
            row += i
            col += j
            if board[row][col] == "X":
                break
            squares += 1
    
    direction(-1, 0)
    reset()
    direction(-1, -1)
    reset()
    direction(0, -1)
    reset()
    direction(1, -1)
    reset()
    direction(1, 0)
    reset()
    direction(1, 1)
    reset()
    direction(0, 1)
    reset()
    direction(-1, 1)
    
    #inputValue = data.get("input");
    #result = inputValue * inputValue
    logging.info("My result :{}".format(squares))



    return json.dumps(squares)

