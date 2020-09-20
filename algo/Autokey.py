lower_alpha = "abcdefghijklmnopqrstuvwxyz"
upper_alpha = lower_alpha.upper()


def generate_key(msg, key):
    i = 0
    while True:
        if len(key) == len(msg):
            break
        else:
            key += msg[i]
            i += 1
    return key


def encrypt(msg, key):
    ciphertext = ''
    pt = msg.replace(' ', '')
    k = generate_key(pt, key.replace(' ', ''))
    for i in range(len(pt)):
        if (pt[i].isupper() and k[i % len(k)].isupper()):
            ciphertext += chr((upper_alpha.index(pt[i]) +
                               upper_alpha.index(k[i])) % (26) + 65)
        if (pt[i].isupper() and k[i % len(k)].islower()):
            ciphertext += chr((upper_alpha.index(pt[i]) +
                               lower_alpha.index(k[i])) % (26) + 65)
        if (pt[i].islower() and k[i % len(k)].islower()):
            ciphertext += chr((lower_alpha.index(pt[i]) +
                               lower_alpha.index(k[i])) % (26) + 97)
        if (pt[i].islower() and k[i % len(k)].isupper()):
            ciphertext += chr((lower_alpha.index(pt[i]) +
                               upper_alpha.index(k[i])) % (26) + 97)
    return ciphertext,k


def decrypt(msg, key):
    plaintext = ""
    ct = msg.replace(" ", "")
    k = generate_key(ct, key.replace(" ", ""))
    for i in range(len(ct)):
        if ct[i].isupper() and k[i].isupper():
            plaintext += chr(
                ((upper_alpha.index(ct[i]) - upper_alpha.index(k[i])) + 26) % (26) + 65
            )
        if ct[i].isupper() and k[i].islower():
            plaintext += chr(
                ((upper_alpha.index(ct[i]) - lower_alpha.index(k[i])) + 26) % (26) + 65
            )
        if ct[i].islower() and k[i].islower():
            plaintext += chr(
                ((lower_alpha.index(ct[i]) - lower_alpha.index(k[i])) + 26) % (26) + 97
            )
        if ct[i].islower() and k[i].isupper():
            plaintext += chr(
                ((lower_alpha.index(ct[i]) - upper_alpha.index(k[i])) + 26) % (26) + 97
            )
    return plaintext,k
