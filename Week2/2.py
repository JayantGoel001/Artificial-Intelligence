def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


if __name__ == '__main__':
    a = int(input("Enter value of A:\n"))
    b = int(input("Enter value of B:\n"))

    gcd = GCD(a, b)
    lcm = (a * b) // gcd

    print("Greatest Common Divisor : ", gcd)
    print("Lowest Common Multiple :", lcm)