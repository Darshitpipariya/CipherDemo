import numpy as np


def message( msg, dim):
    ms = []
    msg = msg.replace(" ", "")
    ind = 0
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    upper_alpha = lower_alpha.upper()
    for index in range(0, len(msg), dim):
        messageVector = [[""] for i in range(dim)]
        for j in range(dim):
            if index < len(msg):
                if msg[index].isupper():
                    messageVector[j][0] = upper_alpha.index(msg[index])
                    index += 1
                else:
                    messageVector[j][0] = lower_alpha.index(msg[index])
                    index += 1
            else:
                messageVector[j][0] = ind
                ind += 1
                index += 1
        ms.append(messageVector)
    return ms


def key_matrix( key, dim):
    k_matrix = []
    k = key.replace(" ", "")
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    upper_alpha = lower_alpha.upper()
    index = 0
    ind = 0
    for i in range(dim):
        l = []
        for j in range(dim):
            if index < len(k):
                if k[index].isupper():
                    l.append(upper_alpha.index(k[index]))
                    index += 1
                else:
                    l.append(lower_alpha.index(k[index]))
                    index += 1
            else:
                l.append(ind)
                ind += 1
        k_matrix.append(l)
    return k_matrix


def deter( k_matrix):
    a = np.array(k_matrix)
    return int(round(np.linalg.det(a)))


def inver_mat( k_matrix):
    a = np.array(k_matrix)
    a = np.linalg.inv(a)
    d = deter(k_matrix)
    a = deter(k_matrix) * a
    x = 1
    while True:
        if (d * x) % 26 == 1:
            break
        x += 1
    a = (a * x) % 26
    x = []
    for i in a.tolist():
        b = []
        for j in i:
            b.append(int(round(j)))
        x.append(b)
    return x


def mat_mul( k_matrix, message_matrix):
    arr1 = np.array(k_matrix)
    arr2 = np.array(message_matrix)
    arr_result = np.matmul(arr1, arr2)
    arr_result = arr_result % 26
    return arr_result.tolist()


def encrypt( plaintext, key, dim):
    k_m = key_matrix(key, dim)
    p_ve = message(plaintext, dim)
    cipher = []
    c = []
    ct = ""
    for i in p_ve:
        cipher.extend(mat_mul(k_m, i))
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    upper_alpha = lower_alpha.upper()
    for i in cipher:
        for j in i:
            ct += lower_alpha[j]
    return ct


def decrypt( ciphertext, key, dim):
    k_m = key_matrix(key, dim)
    # decryption not possible
    if deter(k_m) == 0 or deter(k_m) == 13 or deter(k_m) % 2 == 0:
        return "Not possible"
    else:
        k_m = inver_mat(k_m)
        p_ve = message(ciphertext, dim)
        cipher = []
        c = []
        ct = ""
        for i in p_ve:
            cipher.extend(mat_mul(k_m, i))
        lower_alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in cipher:
            for j in i:
                ct += lower_alpha[j]
        return ct

