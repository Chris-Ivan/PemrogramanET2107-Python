def handleUpperCase(num, shift):
    num += shift
    if num < ord("A"):
        num += 26
    elif num > ord("Z"):
        num -= 26
    return num


def handleLowerCase(num, shift):
    num += shift
    if num < ord("a"):
        num += 26
    elif num > ord("z"):
        num -= 26
    return num


def findShift(idx):
    if (idx % 3 == 1):
        return 3
    elif (idx % 3 == 2):
        return -3
    return 4


def encrypt(message):
    encrypted = ""
    for (idx, char) in enumerate(message, 1):
        if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            shift = findShift(idx)
            num = ord(char)
            temp = handleUpperCase(num, shift) if char.isupper(
            ) else handleLowerCase(num, shift)
            encrypted += chr(temp)
        else:
            encrypted += char
    print(encrypted)
