import random


def startingPlayer():
    return random.randint(0, 1) # chooses which player starts


def updateBoard(board, pos, turn):
    if turn == 0: # updates board based on turn
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


def main():
    player1 = ""
    player2 = ""
    pscores = [0, 0]
    game = True
    while player1 == player2: # checks that player1 isn't the same as player2
        player1 = input("Enter the name of player1")
        player2 = input("Enter the name of player2")
    turn = startingPlayer() # randomly assigns the starting player
    players = (player1, player2)
    while game: # while game is being played
        board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        pmoves = [[], []]
        while not boardFull(board):
            print(f"{players[turn]}'s turn!")
            pos = -1
            while pos > 9 or pos < 0:
                try:
                    printBoard(board)
                    pos = int(input("Enter move(1-9)"))
                except ValueError: #stops crashing if user enters string input
                    pos = -1
            if freeSpace(board, pos): # if space is free: switch turns, add the move to an array and update the board
                pmoves[turn].append(pos)
                updateBoard(board, pos, turn)
                turn = invert(turn)
            else:
                print("Space not available, try again!")
            if Winner(pos, pmoves[invert(turn)]):
                print(players[invert(turn)], " wins!")
                pscores[invert(turn)] += 1
                break
        printBoard(board)
        if boardFull(board) and not Winner(pos, pmoves[invert(turn)]):
            print("It's a draw")
        again = ""
        while again != "y" and again != "n":
            again = input("Play again?(Y/n)").lower()
            if again == "n":
                game = False
            elif again == "y":
                pass
            else:
                print("Invalid input. Please enter (Y) or (N)")
    print("Final Scores!")
    print(f"{players[0]}: {pscores[0]}!")
    print(f"{players[1]}: {pscores[1]}!")


main()
