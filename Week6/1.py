# Constraints
def carry_remainder(x, y, z=0):
    return (x + y + z) // 10, (x + y + z) % 10


def solutionReached(characters, carry, l):
    carry['1'], l[characters['L']] = carry_remainder(l[characters['G']], l[characters['R']])
    carry['2'], l[characters['L']] = carry_remainder(l[characters['N']], l[characters['O']], carry['1'])
    carry['3'], l[characters['E']] = carry_remainder(l[characters['I']], l[characters['O']], carry['2'])
    carry['4'], l[characters['B']] = carry_remainder(l[characters['R']], l[characters['D']], carry['3'])

    result = (l[characters['G']] + l[characters['R']] == 10 * carry['1'] + l[characters['L']]) and (
            l[characters['N']] + l[characters['O']] + carry['1'] == 10 * carry['2'] + l[characters['L']]) and (
                     l[characters['I']] + l[characters['O']] + carry['2'] == 10 * carry['3'] + l[characters['E']]) and (
                     l[characters['R']] + l[characters['D']] + carry['3'] == l[characters['B']] and carry['4'] == 0)

    d = {}
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            return False

    return result


def isSafe(i, x, l):
    if i in l:
        return False
    else:
        if x < len(l):
            return True
        else:
            return False


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
        '3': 0,
        '4': 0
    }
    l = [-1 for _ in range(len(characters))]
    if solvePuzzleUtil(0, l, carry, characters):
        reverse_map = {value: key for key, value in characters.items()}
        for i in range(len(l)):
            print(reverse_map[i], ":", l[i])
    else:
        print("Solution Does Not Exists.")


def solvePuzzleUtil(x, l, carry, characters):
    if x == len(l) and solutionReached(characters, carry, l):
        return True

    for i in range(0, 10):
        if isSafe(i, x, l):
            l[x] = i
            if solvePuzzleUtil(x + 1, l, carry, characters):
                return True
            l[x] = -1

    return False


solvePuzzle()
