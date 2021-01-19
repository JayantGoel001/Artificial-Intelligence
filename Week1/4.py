def isVowel(ch):
    ch = ch.lower()
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        return True
    else:
        return False


if __name__ == '__main__':
    ch = input("Enter a Character:")
    print(isVowel(ch))
