def isPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    string = input()
    print(isPalindrome(string))