def nearly_equal(string1, string2):
    d = {}
    for character in string1:
        if character in d:
            d[character] += 1
        else:
            d[character] = 1

    for character in string2:
        if character in d:
            d[character] -= 1

    count = 0
    for key, value in d.items():
        if value < 0 or count > 2:
            return False
        count += value

    return True


if __name__ == '__main__':
    str1 = input("Enter The First String:\n")
    str2 = input("Enter The Second String:\n")

    print("Are String Nearly Equal ?: ", nearly_equal(str1, str2))
