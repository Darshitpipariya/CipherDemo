def encrypt(msg, step):
    result = ""
    for word in msg.split():
        for i in word:
            if i.isupper():
                result += chr(((ord(i) + step - 65) % 26) + 65)
            else:
                result += chr(((ord(i) + step - 97) % 26) + 97)
        result += " "
    return result

def decrypt(msg, step):
    result = ""
    for word in msg.split():
        for i in word:
            if i.isupper():
                result += chr((((ord(i) - step - 65) + 26) % 26) + 65)
            else:
                result += chr((((ord(i) - step - 97) + 26) % 26) + 97)
        result += " "
    return result

