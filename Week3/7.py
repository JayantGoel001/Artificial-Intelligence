def isSafe(x, y, initial, final):
    return 0 <= x < 3 and 0 <= y < 3


def printPath(l):
    for i in l:
        for j in i:
            print(j, end=" ")
        print()
    print()


def isEqual(intial, final):
    for i in range(3):
        for j in range(3):
            if intial[i][j] != final[i][j]:
                return False
    return True


def solve(initial, final, blankX, blankY, outputPath):
    XY = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    if not isEqual(initial, final):
        for x, y in XY:
            if isSafe(blankX + x, blankY + y, initial, final):
                temp = initial
                temp[blankX + x][blankY + y], temp[blankX][blankY] = temp[blankX][blankY], temp[blankX + x][blankY + y]
                outputPath.append(temp)
                printPath(temp)
                solve(temp, final, blankX + x, blankY + y, outputPath)
                outputPath.pop()
    else:
        return outputPath


if __name__ == '__main__':
    initial = [[2, 8, 3],
               [1, 6, 4],
               [7, 0, 5]]

    final = [[1, 2, 3],
             [8, 0, 4],
             [7, 6, 5]]

    blankX = 2
    blankY = 1

    outputPath = []

    outputPath = solve(initial, final, blankX, blankY, outputPath)

    for i in range(len(outputPath)):
        printPath(outputPath[i])
