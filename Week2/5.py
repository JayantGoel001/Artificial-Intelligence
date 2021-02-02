limit = 4000000

l = [1, 2]
prev = 1
curr = 2


def generate(prev, curr):
    prevX = 2 * curr + prev
    currX = 3 * curr + 2 * prev
    return prevX, currX


s = 2
while True:
    prev, curr = generate(prev, curr)
    if curr<limit:
        s += curr
    else:
        break

print(s)