def max(a, b):
    if a > b:
        return a
    else:
        return b


def max_of_three(a, b, c):
    if a > b:
        return max(a, c)
    else:
        return max(b, c)


if __name__ == '__main__':
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = int(input("Enter c:"))
    print("Maximum number is:", max_of_three(a, b, c))
