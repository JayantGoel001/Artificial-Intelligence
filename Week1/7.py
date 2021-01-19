def reverse(string):
    for i in range(len(string)):
        print(string[len(string) - i - 1],end="")


if __name__ == '__main__':
    string = input()
    print(reverse(string))
