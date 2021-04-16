x = 'X'
o = 'O'
e = '-'


def isMoveLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == e:
                return True

    return False


def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == x:
                return 10
            elif board[row][0] == o:
                return -10

    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == x:
                return 10
            elif board[0][col] == o:
                return -10

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == x:
            return 10
        elif board[0][0] == o:
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == x:
            return 10
        elif board[0][2] == o:
            return -10

    return 0


def minimax(board, depth, isMax):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score

    if not isMoveLeft(board):
        return 0

    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == e:
                    board[i][j] = x
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = e
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == e:
                    board[i][j] = o
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = e
        return best

def getBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == e:
                board[i][j] = x
                moveVal = minimax(board, 0, False)
                board[i][j] = e

                if moveVal > bestVal:
                    bestVal = moveVal
                    bestMove = (i, j)

    return bestMove


if __name__ == '__main__':
    board = [
        [x, o, x],
        [x, e, o],
        [o, e, e]
    ]

    moveX, moveY = getBestMove(board)
    print("The Best Move is:\n")
    print("Row:", moveX, "\nCol:", moveY)
