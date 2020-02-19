def freeSpaces(board):
    spaces = []
    for i in range(len(board)):
        if board[i] == "-":
            spaces.append(i + 1)
    if not spaces:
        return False
    return spaces


def invert(turn):  # used to switch turns after each move
    if turn == "X":
        return "O"
    return "X"


def getPiece(turn):
    turns = {-1: "X", 1: "O"}
    return turns[turn]


def getTurn(piece):
    pieces = {"X": -1, "O": 1}
    return pieces[piece]


def updateBoard(board, pos, turn):
    board[pos - 1] = turn
    return board


def boardFull(board):
    for i in board:
        if i == "-":
            return False
    return True


# def checkCase(case, pmoves):
#     num = 0
#     for i in case:
#         if int(i) in pmoves:
#             num += 1
#     if num == 3:
#         return True
#     return False
#
#
# def winner(board, pos, turn):
#     pmoves =[[],[]]
#     for i in range(len(board)):
#         if i == "X":
#             pmoves[0].append(i)
#         elif i == "O":
#             pmoves[1].append(i)
#     pmoves = pmoves[turn]
#     row = ["123", "456", "789"]
#     col = ["147", "258", "369"]
#     diag = ["159", "357"]
#     for i in row:
#         if str(pos) in i:
#             case = i
#             if checkCase(case, pmoves):
#                 return True
#
#     for i in col:
#         if str(pos) in i:
#             case = i
#             if checkCase(case, pmoves):
#                 return True
#
#     for i in diag:
#         if str(pos) in i:
#             case = i
#             if checkCase(case, pmoves):
#                 return True
#     return False

def checkWinner(board):
    # horizontal check
    # returns -1 if X wins, 1 if O wins
    for i in range(0, 7, 3):
        if board[0 + i] == board[1 + i] == board[2 + i] and board[0+i] != "-":
            return getTurn(board[0 + i])
    # vertical check
    for i in range(3):
        if board[0 + i] == board[3 + i] == board[6 + i] and board[0+i] != "-":
            return getTurn(board[0 + i])
    # diagonal check
    if board[0] == board[4] == board[8] and board[0] != "-":
        return getTurn(board[0])
    if board[2] == board[4] == board[6] and board[2] != "-":
        return getTurn(board[2])
    # returns 0 for draw
    if boardFull(board):
        return 0

