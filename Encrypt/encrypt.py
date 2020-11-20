# Christopher Ivan Gunardi
# 18119025
# Program Enkripsi-Dekripsi


def handleUpperCase(num, shift):  # untuk upper case
    num += shift
    if num < ord("A"):
        num += 26
    elif num > ord("Z"):
        num -= 26
    return num


def handleLowerCase(num, shift):  # untuk lower case
    num += shift
    if num < ord("a"):
        num += 26
    elif num > ord("z"):
        num -= 26
    return num


def findShift(idx, shift1, shift2, shift3):  # untuk mencari shift
    if (idx % 3 == 1):
        return shift2
    elif (idx % 3 == 2):
        return shift3
    return shift1


def cipher(message, shift1, shift2, shift3):  # fungsi utama
    encrypted = ""
    for (idx, char) in enumerate(message, 1):
        if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            shift = findShift(idx, shift1, shift2, shift3)
            num = ord(char)
            temp = handleUpperCase(num, shift) if char.isupper(
            ) else handleLowerCase(num, shift)
            encrypted += chr(temp)
        else:
            encrypted += char
    return encrypted


def encode(message, lower=False):  # fungsi encode yang menerima huruf kapital
    if (lower):  # jika dimasukan lower=True, maka hasil encode menjadi huruf kecil
        message = message.lower()
    return cipher(message, 4, 3, -3)


def decode(message):  # fungsi decode
    return cipher(message, -4, -3, 3)


texts = ["HELLO WORLD", "Hello, world!", "pA$$w0rD", "tes", "T3st"]

print("MENERIMA UPPER CASE")
print()
for text in texts:  # Program normal
    print("Text:", text)
    encoded = encode(text)
    print("Hasil enkripsi:", encoded)
    print("Hasil dekripsi:", decode(encoded))
    print()

print("SEMUANYA LOWER CASE")
print()
for text in texts:  # Semuanya lower case
    print("Text:", text)
    encoded = encode(text, lower=True)
    print("Hasil enkripsi:", encoded)
    print("Hasil dekripsi:", decode(encoded))
    print()
