# Constraints
def carry_remainder(x, y, z=0):
    return (x + y + z) // 10, (x + y + z) % 10


def solutionReached(characters, carry, l):
    carry['1'], l[characters['L']] = carry_remainder(l[characters['G']], l[characters['R']])
    carry['2'], l[characters['L']] = carry_remainder(l[characters['N']], l[characters['O']], carry['1'])
    carry['3'], l[characters['E']] = carry_remainder(l[characters['I']], l[characters['O']], carry['2'])
    carry['4'], l[characters['B']] = carry_remainder(l[characters['R']], l[characters['D']])

    return (l[characters['G']] + l[characters['R']] == 10 * carry['1'] + l[characters['L']]) and (
            l[characters['N']] + l[characters['O']] + carry['1'] == 10 * carry['2'] + l[characters['L']]) and (
                   l[characters['I']] + l[characters['O']] + carry['2'] == 10 * carry['3'] + l[characters['E']]) and (
                   l[characters['R']] + l[characters['D']] + carry['3'] == l[characters['B']])


def isSafe(x, l):
    if x in l:
        return False
    return True


def solvePuzzle():
    # values ranging form 0 to 9
    characters = {
        'R': 0,
        'I': 1,
        'N': 2,
        'G': 3,
        'D': 4,
        'O': 5,
        'B': 6,
        'E': 7,
        'L': 8
    }
    # values ranging from 0 to 1
    carry = {
        '1': 0,
        '2': 0,
        '3': 0
    }
    l = [0 for _ in range(len(characters))]
    if solvePuzzleUtil(0, l, carry, characters):
        print(l)


def solvePuzzleUtil(x, l, carry, characters):
    if x == len(l)-1 and solutionReached(characters, carry, l):
        return True

    for i in range(1, 10):
        if isSafe(i, l) and x<len(l):
            l[x] = i
            print(l)
            solvePuzzleUtil(x + 1, l, carry, characters)
            l[x] = 0

    return False


solvePuzzle()
