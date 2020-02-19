import random
import evaluate


def maxi(lst):
    max_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val


def mini(lst):
    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val


def minimax(board, depth, maximising):
    if evaluate.checkWinner(board) is not None:
        return evaluate.checkWinner(board)
    else:
        if maximising:
            bestscore = -100
        else:
            bestscore = 100
        for pos in evaluate.freeSpaces(board):
            if maximising:
                board[pos-1] = "O"
                score = minimax(board, depth + 1, False)
                bestscore = max(score, bestscore)

            else:
                board[pos-1] = "X"
                score = minimax(board, depth + 1, True)
                bestscore = min(score, bestscore)
            board[pos-1] = "-"
    return bestscore


def compMove(board, turn):
    bestscore = -100
    for pos in evaluate.freeSpaces(board):
        board = evaluate.updateBoard(board, pos, turn)
        score = minimax(board, 0, False)
        board[pos - 1] = "-"
        if score > bestscore:
            bestscore = score
            bestmove = pos
    return bestmove

