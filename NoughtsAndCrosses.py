import random
import CompAI


def startingPlayer():
    return random.randint(0, 1)  # chooses which player starts


def updateBoard(board, pos, turn):
    if turn == 0:  # updates board based on turn
        piece = "X"
    else:
        piece = "O"
    board[pos - 1] = piece
    return board


def freeSpace(board, pos):
    if board[pos - 1] == "-":
        return True
    return False


def printBoard(board):
    for j in range(0, 9, 3):
        for i in range(3):
            print(board[i + j], end=" ")
        print("")


def invert(turn):  # used to switch turns after each move
    if turn == 1:
        return 0
    return 1


def boardFull(board):
    for i in board:
        if i == "-":
            return False
    return True


def checkCase(case, pmoves):
    num = 0
    for i in case:
        if int(i) in pmoves:
            num += 1
    if num == 3:
        return True
    return False


def Winner(pos, pmoves):
    row = ["123", "456", "789"]
    col = ["147", "258", "369"]
    diag = ["159", "357"]
    for i in row:
        if str(pos) in i:
            case = i
            if checkCase(case, pmoves):
                return True

    for i in col:
        if str(pos) in i:
            case = i
            if checkCase(case, pmoves):
                return True

    for i in diag:
        if str(pos) in i:
            case = i
            if checkCase(case, pmoves):
                return True
    return False


# def main():
#     player1 = ""
#     player2 = ""
#     pscores = [0, 0]
#     game = True
#     mode = input("Computer(C) or Human(H)?").upper()
#     if mode == "C":
#         Computer = True
#         player1 = input("Enter the name of player1")
#         player2 = "Computer"
#     elif mode == "H":
#         Computer = False
#         while player1 == player2:  # checks that player1 isn't the same as player2
#             player1 = input("Enter the name of player1")
#             player2 = input("Enter the name of player2")
#     else:
#         print("Invalid input, defaulting to Computer")
#         player1 = input("Enter the name of player1")
#         player2 = "Computer"
#         Computer = True
#
#     turn = startingPlayer()  # randomly assigns the starting player
#     players = (player1, player2)
#     while game:  # while game is being played
#         board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
#         pmoves = [[], []]
#         while not boardFull(board):
#             if not Computer:
#                 print(f"{players[turn]}'s turn!")
#             elif Computer and turn == 0:
#                 print(f"{players[turn]}'s turn!")
#             pos = -1
#             if turn == 1 or not Computer:
#                 while pos > 9 or pos < 0:
#                     try:
#                         printBoard(board)
#                         pos = int(input("Enter move(1-9)"))
#                     except ValueError:  # checks for invalid inputs
#                         pos = -1
#             else:
#                 pos = CompAI.compMove(board)
#             if freeSpace(board, pos):  # if space is free: switch turns, add the move to an array and update the board
#                 pmoves[turn].append(pos)
#                 updateBoard(board, pos, turn)
#
#             else:
#                 print("Space not available, try again!")
#             winner = Winner(pos, pmoves[turn])
#             if winner and not Computer:
#                 print(players[turn], " wins!")
#                 pscores[turn] += 1
#                 break
#             elif winner and Computer:
#                 print(players[invert(turn)], "wins!")
#                 pscores[invert(turn)] += 1
#             turn = invert(turn)
#         printBoard(board)
#         if boardFull(board) and not Winner(pos, pmoves[invert(turn)]):
#             print("It's a draw")
#
#         again = ""
#         while again != "y" and again != "n":
#             again = input("Play again?(Y/n)").lower()
#             if again == "n":
#                 game = False
#             elif again == "y":
#                 pass
#             else:
#                 print("Invalid input. Please enter (Y) or (N)")
#     print("Final Scores!")
#     print(f"{players[0]}: {pscores[0]}")
#     print(f"{players[1]}: {pscores[1]}")
#
#
# main()
def Players():
    players = ["", ""]
    mode = ""
    while mode != "C" and mode != "H":
        mode = input("Enter mode: Computer(C) or Human(H)").upper()
    players[0] = input("Enter name of player1")
    players[1] = players[0]
    if mode == "H":
        while players[0] == players[1]:
            players[1] = input("Enter name of player2")
        computer = False
    else:
        players[1] = "Computer"
        computer = True

    return players, computer


def position(board):
    pos = -1
    while pos < 1 or pos > 9:
        try:
            printBoard(board)
            pos = int(input("Enter position(1-9)"))
        except ValueError:
            printBoard(board)
            print("Invalid input, must be integer")
            pos = -1
    if freeSpace(board, pos):
        return pos
    else:
        printBoard(board)
        print("Space unavailable")
        position(board)


def repeat():
    again = ""
    while again != "Y" and again != "N":
        again = input("Play again?(Y/n)")
    if again == "Y":
        return True
    return False


def main():
    players, computer = Players()
    turn = startingPlayer()
    games = True
    pscores = [0, 0]
    while games:
        board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        pmoves = [[], []]
        while not boardFull(board):
            if not computer or turn == 0:
                print(f"{players[turn]}'s turn!")
                pos = position(board)
            else:
                pos = CompAI.compMove(board)
            pmoves[turn].append(pos)
            updateBoard(board, pos, turn)
            if Winner(pos, pmoves[turn]):
                print(f"{players[turn]} wins!")
                pscores[turn] += 1
                break
            else:
                turn = invert(turn)
        if not Winner(pos, pmoves[turn]):
            printBoard(board)
            print("It's a draw!")
        print("Scores:")
        print(f"{players[0]}: {pscores[0]}")
        print(f"{players[1]}: {pscores[1]}")
        games = repeat()


main()
