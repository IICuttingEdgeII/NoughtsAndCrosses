import random
def spaces(board):
    spaces = []
    for i in range(len(board)):
        if board[i] == "-":
           spaces.append(i+1)
    return spaces

def compMove(board):
    return random.choice(spaces(board))

