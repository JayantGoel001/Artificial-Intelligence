def isCon(ch):
    ch = ch.lower()
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch==' ':
        return False
    else:
        return True


def translate(text):
    string = ""
    for i in range(0, len(text)):
        if isCon(text[i]):
            string += text[i] + "o" + text[i]
        else:
            string += text[i]
    return string


if __name__ == '__main__':
    text = input("enter a text:")
    print(translate(text))
