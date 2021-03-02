class TicTacToe:
    def __init__(self):
        self.board = []
        for i in range(3):
            self.board.append([" ", " ", " "])

    def __str__(self):
        return str(self.board)

    def makeMove(self, player, pos):
        if self.board[pos[0]][pos[1]] == " ":
            self.board[pos[0]][pos[1]] = player
            return True
        else:
            return False

    def hasWon(self, player):
        for i in range(3):
            count = 0
            for j in range(3):
                if self.board[i][j] == player:
                    count += 1

            if count == 3:
                return True

        for i in range(3):
            count = 0
            for j in range(3):
                if self.board[j][i] == player:
                    count += 1

            if count == 3:
                return True

        count = 0
        for i in range(3):
            if self.board[i][i] == player:
                count += 1

        if count == 3:
            return True

        count = 0
        for i in range(3):
            if self.board[3 - i - 1][i] == player:
                count += 1

        if count == 3:
            return True

        return False

    def gameOver(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    return False
        return True

    def clear(self):
        self.board.clear()

    def printBoard(self):
        for i in range(3):
            for j in range(3):
                if j != 2:
                    print(self.board[i][j], end=" | ")
                else:
                    print(self.board[i][j],end="")
            if i != 2:
                print("\n---------")
        print()


if __name__ == '__main__':
    t = TicTacToe()
    OddEven = 1
    while not t.gameOver():
        x, y = map(int, input("Enter the pos:  x,y = ").split(","))
        if OddEven % 2 == 1:
            if t.makeMove(player="X", pos=[x, y]):
                OddEven += 1
        else:
            if t.makeMove(player="O", pos=[x, y]):
                OddEven += 1

        t.printBoard()

        if t.hasWon("X"):
            print("Player One(X) Won!!!")
            break
        if t.hasWon("O"):
            print("Player Two(O) Won!!!")
            break
