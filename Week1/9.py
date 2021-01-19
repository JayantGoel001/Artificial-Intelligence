def histogram(l):
    for i in l:
        print("*" * i)


if __name__ == '__main__':
    l = list(map(int, input().split()))
    histogram(l)