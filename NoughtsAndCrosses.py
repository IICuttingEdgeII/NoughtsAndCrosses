import random
import evaluate
import CompAI
import time


def turnIndex(turn):
    # function solely for indexing in lists e.g players
    # not to be confused with getTurn
    # because in this instance lst[-1] == lst[1]
    index = {"X": 0, "O": 1}
    return index[turn]


def playerToIndex(turn):
    index = {-1: 0, 1: 1}
    return index[turn]


def startingPlayer():
    return random.randint(0, 1)  # chooses which player starts


def freeSpace(board, pos):
    if board[pos - 1] == "-":
        return True
    return False


def printBoard(board):
    for j in range(0, 9, 3):
        for i in range(3):
            print(board[i + j], end=" ")
        print("")


def playerInit():
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
    while (pos < 1 or pos > 9) or not freeSpace(board, pos):  # checks if space free and valid
        try:
            printBoard(board)
            pos = int(input("Enter position(1-9)"))
        except ValueError:
            printBoard(board)
            print("Invalid input, must be integer")
            pos = -1
    return pos


def repeat():
    again = ""
    while again != "Y" and again != "N":
        again = input("Play again?(Y/n)").upper()
    if again == "Y":
        return True
    return False


def main():
    players, computer = playerInit()
    turn = "X"
    games = True
    pscores = [0, 0]
    while games:
        board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        while not evaluate.boardFull(board) and evaluate.checkWinner(board) is None:
            if not computer or turn == "X":
                print(f"{players[turnIndex(turn)]}'s turn!")
                pos = position(board)  # taken as int from 1-9
            else:
                print("thinking...")
                time.sleep(1)  # delay for realisticness
                pos = CompAI.compMove(board, turn)
            board[pos - 1] = turn
            turn = evaluate.invert(turn)
        if evaluate.checkWinner(board) == 0:
            printBoard(board)
            print("It's a draw!")
        else:
            winner = playerToIndex(evaluate.checkWinner(board))
            printBoard(board)
            print(f"{players[winner]} wins!")
            pscores[winner] += 1
        print("Scores:")
        print(f"{players[0]}: {pscores[0]}")
        print(f"{players[1]}: {pscores[1]}")
        games = repeat()


main()
