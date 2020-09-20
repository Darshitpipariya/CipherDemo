def encrypt(plainText,key):
    key="".join(key.lower().split(" "))
    key_ma=getKeyMatrix(key)
    plainText="".join(plainText.lower().split(" "))
    plainText1=getProcessPlaintext(list(plainText))
    plainText1="".join(plainText1)
    ct=[]
    for p in range(0, len(plainText1), 2):
        c1,c2,r1,r2=0,0,0,0
        for i in range(5):
            for j in range(5):
                if plainText1[p] == key_ma[i][j]:
                    r1,c1 = i,j
                if plainText1[p + 1] == key_ma[i][j]:
                    r2,c2 = i,j
        if c1 == c2:
            ct.append(key_ma[(r1 + 1) % 5][c1])
            ct.append(key_ma[(r2 + 1) % 5][c2])
        elif r1 == r2:
            ct.append(key_ma[r1][(c1 + 1) % 5])
            ct.append(key_ma[r2][(c2 + 1) % 5])
        else:
            ct.append(key_ma[r1][c2])
            ct.append(key_ma[r2][c1])
    return "".join(ct)

def decrypt(cipherText,key):
    key="".join(key.lower().split(" "))
    key_ma=getKeyMatrix(key)
    pt=[]
    for p in range(0, len(cipherText), 2):
        c1,c2,r1,r2=0,0,0,0
        for i in range(5):
            for j in range(5):
                if cipherText[p] == key_ma[i][j]:
                    r1, c1 = i, j
                if cipherText[p + 1] == key_ma[i][j]:
                    r2, c2 = i, j
        if c1 == c2:
            pt.append(key_ma[(r1 - 1) % 5][c1])
            pt.append(key_ma[(r2 - 1) % 5][c2])
        elif r1 == r2:
            pt.append(key_ma[r1][(c1 - 1) % 5])
            pt.append(key_ma[r2][(c2 - 1) % 5])
        else:
            pt.append(key_ma[r1][c2])
            pt.append(key_ma[r2][c1])
    return "".join(pt)

def getKeyMatrix(key):
    key_id = []
    for i in key:
        if i not in key_id:
            key_id.append(i)
    for i in range(26):
        if chr(i + 97) not in key_id:
            if chr(i + 97) != 'j':
                key_id.append(chr(i + 97))
    k = 0
    key_matrix = [[None] * 5 for i in range(5)]
    for i in range(5):
        for j in range(5):
            key_matrix[i][j] = key_id[k]
            k += 1
    return key_matrix
def getProcessPlaintext(plainText):
    if len(plainText) % 2 != 0:
        if plainText[-1] == 'x':
            plainText.append('z')
        else:
            plainText.append('x')
    plainText1 = []
    for i in plainText:
        if i == 'j':
            plainText1.append('i')
        else:
            plainText1.append(i)
    for i in range(0, len(plainText1), 2):
        if plainText1[i] == plainText1[i + 1]:
            if plainText1[i] == 'x':
                plainText1.insert(i + 1, 'z')
            else:
                plainText1.insert(i + 1, 'x')
    return plainText1