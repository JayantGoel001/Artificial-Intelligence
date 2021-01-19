def sum(l):
    add = 0
    for i in l:
        add += i

    return add


def mutliply(l):
    prod = 1
    for i in l:
        prod *= i

    return prod


if __name__ == '__main__':
    l = list(map(int, input().split()))
    print(sum(l))
    print(mutliply(l))
