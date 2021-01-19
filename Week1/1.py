def max(a, b):
    if a > b:
        return a
    else:
        return b


if __name__ == '__main__':
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print("Maximum number is:", max(a, b))
