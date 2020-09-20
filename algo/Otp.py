# key and msg size must be same msg witout space


def encrypt(msg, key):
    msg = msg.lower()
    key = key.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    for i in range(len(msg)):
        c = alphabet.find(msg[i]) ^ alphabet.find(key[i])
        ciphertext += alphabet[c % 26]
    return ciphertext


def decrypt(msg, key):
    msg = msg.lower()
    key = key.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    for i in range(len(msg)):
        c = alphabet.find(msg[i]) ^ alphabet.find(key[i])
        ciphertext += alphabet[c % 26]
    return ciphertext

