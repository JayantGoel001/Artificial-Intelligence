def length(x):
    len = 0
    for _ in x:
        len += 1
    return len


if __name__ == '__main__':
    x = input("Enter a string:")
    print("Length = " + str(length(x)))

    x = list(map(int, input("Enter a list:").split()))
    print("Length = " + str(length(x)))
