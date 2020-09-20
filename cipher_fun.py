
import numpy as np
import math

#Caesar Cipher
class Caesar:
    def __init__(self): pass


    def encrypt(self,msg, step):
        result = ""
        for word in msg.split():
            for i in word:
                if (i.isupper()):
                    result += chr(((ord(i)+step-65) % 26)+65)
                else:
                    result += chr(((ord(i)+step-97) % 26)+97)
            result+=" "
        return result


    def deycrypt(self,msg,step):
        result = ""
        for word in msg.split():
            for i in word:
                if (i.isupper()):
                    result += chr((((ord(i)-step-65)+26) % 26)+65)
                else:
                    result += chr((((ord(i)-step-97)+26) % 26)+97)
            result+=" "
        return result



#Monoalphabetic
class Monoalphabetic:
    def __init__(self): pass


    mono_dict = {
        "0": "A",
        "1": "D",
        "2": "C",
        "3": "B",
        "4": "E",
        "5": "G",
        "6": "H",
        "7": "F",
        "8": "I",
        "9": "K",
        "a": "J",
        "b": "N",
        "c": "O",
        "d": "M",
        "e": "L",
        "f": "R",
        "g": "Q",
        "h": "P",
        "i": "U",
        "j": "S",
        "k": "T",
        "l": "X",
        "m": "Z",
        "n": "Y",
        "o": "V",
        "p": "W",
        "q": "0",
        "r": "2",
        "s": "1",
        "t": "3",
        "u": "4",
        "v": "7",
        "w": "5",
        "x": "9",
        "y": "8",
        "z": "6",
        "A": "x",
        "B": "z",
        "C": "y",
        "D": "w",
        "E": "v",
        "F": "q",
        "G": "s",
        "H": "r",
        "I": "t",
        "J": "u",
        "K": "p",
        "L": "a",
        "M": "c",
        "N": "d",
        "O": "b",
        "P": "e",
        "Q": "h",
        "R": "g",
        "S": "f",
        "T": "j",
        "U": "i",
        "V": "k",
        "W": "n",
        "X": "m",
        "Y": "l",
        "Z": "o",
        " ": " ",
    }
    mono_dict_invers = dict([(value, key) for key, value in mono_dict.items()])

    def encrypt(self, msg):
        result = ""
        for i in msg:
            result += mono_dict[i]
        return result


    def decrypt(self,msg):
        result = ""
        for i in msg:
            result += mono_dict_invers[i]
        return result



#vigenere
class Vigenere:
    def __init__(self): pass


    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    upper_alpha = lower_alpha.upper()


    def encrypt(self,plaintext,key):
        ciphertext = ""
        pt = plaintext.replace(' ', '')
        k = key.replace(' ', '')
        for i in range(len(pt)):
            if(pt[i].isupper() and k[i % len(k)].isupper()):
                ciphertext += chr((upper_alpha.index(pt[i]) +
                                upper_alpha.index(k[i % len(k)])) % (26)+65)
            if(pt[i].isupper() and k[i % len(k)].islower()):
                ciphertext += chr((upper_alpha.index(pt[i]) +
                                lower_alpha.index(k[i % len(k)])) % (26)+65)
            if(pt[i].islower() and k[i % len(k)].islower()):
                ciphertext += chr((lower_alpha.index(pt[i]) +
                                lower_alpha.index(k[i % len(k)])) % (26)+97)
            if(pt[i].islower() and k[i % len(k)].isupper()):
                ciphertext += chr((lower_alpha.index(pt[i]) +
                                upper_alpha.index(k[i % len(k)])) % (26)+97)
        return ciphertext


    def decrypt(self,ciphertext,key):
        plaintext = ""
        ct = ciphertext.replace(' ', '')
        k = key.replace(' ', '')
        for i in range(len(ct)):
            if(ct[i].isupper() and k[i % len(k)].isupper()):
                plaintext += chr(((upper_alpha.index(ct[i]) -
                                upper_alpha.index(k[i % len(k)]))+26) % (26)+65)
            if(ct[i].isupper() and k[i % len(k)].islower()):
                plaintext += chr(((upper_alpha.index(ct[i]) -
                                lower_alpha.index(k[i % len(k)]))+26) % (26)+65)
            if(ct[i].islower() and k[i % len(k)].islower()):
                plaintext += chr(((lower_alpha.index(ct[i]) -
                                lower_alpha.index(k[i % len(k)]))+26) % (26)+97)
            if(ct[i].islower() and k[i % len(k)].isupper()):
                plaintext += chr(((lower_alpha.index(ct[i]) -
                                upper_alpha.index(k[i % len(k)]))+26) % (26)+97)
        return plaintext



#Autokey
class Autokey:
    def __init__(self): pass
    
    
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    upper_alpha = lower_alpha.upper()
    
    
    def __generate_key(self,msg, key):
        i = 0
        while True:
            if len(key) == len(msg):
                break
            else:
                key += msg[i]
                i += 1
        return key
    
    
    def encrypt(self,msg,key):
        ciphertext=''
        pt = msg.replace(' ', '')
        k=__generate_key(pt,key.replace(' ', ''))
        for i in range(len(pt)):
            if(pt[i].isupper() and k[i % len(k)].isupper()):
                ciphertext += chr((upper_alpha.index(pt[i]) +
                                upper_alpha.index(k[i])) % (26)+65)
            if(pt[i].isupper() and k[i % len(k)].islower()):
                ciphertext += chr((upper_alpha.index(pt[i]) +
                                lower_alpha.index(k[i])) % (26)+65)
            if(pt[i].islower() and k[i % len(k)].islower()):
                ciphertext += chr((lower_alpha.index(pt[i]) +
                                lower_alpha.index(k[i])) % (26)+97)
            if(pt[i].islower() and k[i % len(k)].isupper()):
                ciphertext += chr((lower_alpha.index(pt[i]) +
                                upper_alpha.index(k[i])) % (26)+97)
        return ciphertext
    
    
    def decrypt(self,msg,key):
        plaintext = ""
        ct = msg.replace(' ', '')
        k=__generate_key(ct,key.replace(' ', ''))
        for i in range(len(ct)):
            if(ct[i].isupper() and k[i % len(k)].isupper()):
                plaintext += chr(((upper_alpha.index(ct[i]) -
                                upper_alpha.index(k[i]))+26) % (26)+65)
            if(ct[i].isupper() and k[i % len(k)].islower()):
                plaintext += chr(((upper_alpha.index(ct[i]) -
                                lower_alpha.index(k[i]))+26) % (26)+65)
            if(ct[i].islower() and k[i % len(k)].islower()):
                plaintext += chr(((lower_alpha.index(ct[i]) -
                                lower_alpha.index(k[i]))+26) % (26)+97)
            if(ct[i].islower() and k[i % len(k)].isupper()):
                plaintext += chr(((lower_alpha.index(ct[i]) -
                                upper_alpha.index(k[i]))+26) % (26)+97)
        return plaintext



#One time pad
class Otp:
    #key and msg size must be same msg witout space
    def __init__(self): pass
    
    
    def encrypt(self,msg,key):
        msg=msg.lower()
        key=key.lower()
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        ciphertext = ""
        for i in range(len(msg)):
            c = alphabet.find(msg[i]) ^ alphabet.find(key[i])
            ciphertext += alphabet[c % 26]
        return ciphertext
    
    
    def decrypt(self,msg,key):
        msg=msg.lower()
        key=key.lower()
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        ciphertext = ""
        for i in range(len(msg)):
            c = alphabet.find(msg[i]) ^ alphabet.find(key[i])
            ciphertext += alphabet[c % 26]
        return ciphertext



#playfair
class Playfair:
    def __init__(self):pass
    
    
    def key_genarator(self,key):
        alphabet = 'abcdefghiklmnopqrstuvwxyz'
        key = key.replace(" ", "")
        table = []
        for char in key.lower():
            if char not in table:
                if char == 'j':
                    char = 'i'
                table.append(char)
        for char in alphabet:
            if char not in table:
                table.append(char)
        j = 0
        final = []
        for i in range(5):
            l = []
            for k in range(5):
                if(j < len(table)):
                    l.append(table[j])
                    j += 1
            final.append(l)
        return final
    
    
    def to_diagraph(self,text):
        table = []
        text = text.replace(" ", "")
        for i in range(len(text)-1):
            table.append(text[i])
            if(text[i] == text[i+1]):
                if(text[i] == 'x'):
                    table.append('y')
                else:
                    table.append('x')
        table.append(text[-1])
        if(len(table) % 2 != 0):
            if(text[-1] == 'x'):
                table.append('y')
            else:
                table.append('x')
        l1 = []
        for i in range(0, len(table), 2):
            l1.append([table[i], table[i+1]])
        return l1

    
    def encrypt(self,plaintext,key):
        diagraph = to_diagraph(plaintext)
        key_matrix = key_genarator(key)
        cipher = []
        # find co-ordinates of dia-graph in key metrix
        for d in diagraph:
            e1, e2 = d[0], d[1]
            for i in range(len(key_matrix)):
                if(e1 in key_matrix[i]):
                    j = key_matrix[i].index(e1)
                    e1_x, e1_y = i, j
                if(e2 in key_matrix[i]):
                    j = key_matrix[i].index(e2)
                    e2_x, e2_y = i, j
            if(e1_x == e2_x):
                # if row is same
                e1 = key_matrix[e1_x][(e1_y+1) % 5]
                e2 = key_matrix[e2_x][(e2_y+1) % 5]
            elif(e1_y == e2_y):
                # if column is same
                e1 = key_matrix[(e1_x+1) % 5][e1_y]
                e2 = key_matrix[(e2_x+1) % 5][e2_y]
            else:
                e1 = key_matrix[e1_x][e2_y]
                e2 = key_matrix[e2_x][e1_y]
            cipher.append(e1)
            cipher.append(e2)
        cipher = "".join(i for i in cipher)
        return cipher
    
    
    def decrypt(self,ciphertext,key):
        diagraph = to_diagraph(ciphertext)
        key_matrix = key_genarator(key)
        plaintext = []
        # find co-ordinates of dia-graph in key metrix
        for d in diagraph:
            e1, e2 = d[0], d[1]
            for i in range(len(key_matrix)):
                if(e1 in key_matrix[i]):
                    j = key_matrix[i].index(e1)
                    e1_x, e1_y = i, j
                if(e2 in key_matrix[i]):
                    j = key_matrix[i].index(e2)
                    e2_x, e2_y = i, j
            if(e1_x == e2_x):
                # if row is same
                e1 = key_matrix[e1_x][(e1_y-1) % 5]
                e2 = key_matrix[e2_x][(e2_y-1) % 5]
            elif(e1_y == e2_y):
                # if column is same
                e1 = key_matrix[(e1_x-1) % 5][e1_y]
                e2 = key_matrix[(e2_x-1) % 5][e2_y]
            else:
                e1 = key_matrix[e1_x][e2_y]
                e2 = key_matrix[e2_x][e1_y]
            plaintext.append(e1)
            plaintext.append(e2)
        plaintext = "".join(i for i in plaintext)
        plaintext = plaintext.replace('x', '')
        return plaintext



#hill Cipher
class Hillcipher:
    def __init__(self):pass


    def message(self,msg, dim):
        ms = []
        msg = msg.replace(' ', '')
        ind = 0
        lower_alpha = "abcdefghijklmnopqrstuvwxyz"
        upper_alpha = lower_alpha.upper()
        for index in range(0, len(msg), dim):
            messageVector = [[''] for i in range(dim)]
            for j in range(dim):
                if(index < len(msg)):
                    if(msg[index].isupper()):
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


    def key_matrix(self,key, dim):
        k_matrix = []
        k = key.replace(' ', '')
        lower_alpha = "abcdefghijklmnopqrstuvwxyz"
        upper_alpha = lower_alpha.upper()
        index = 0
        ind = 0
        for i in range(dim):
            l = []
            for j in range(dim):
                if(index < len(k)):
                    if(k[index].isupper()):
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
    def deter(self,k_matrix):
        a = np.array(k_matrix)
        return int(round(np.linalg.det(a)))


    def inver_mat(self,k_matrix):
        a = np.array(k_matrix)
        a = np.linalg.inv(a)
        d = deter(k_matrix)
        a = deter(k_matrix) * a
        x = 1
        while True:
            if((d*x) % 26 == 1):
                break
            x += 1
        a = (a*x) % 26
        x = []
        for i in a.tolist():
            b = []
            for j in i:
                b.append(int(round(j)))
            x.append(b)
        return x


    def mat_mul(self,k_matrix, message_matrix):
        arr1 = np.array(k_matrix)
        arr2 = np.array(message_matrix)
        arr_result = np.matmul(arr1, arr2)
        arr_result = arr_result % 26
        return arr_result.tolist()


    def encrypt(self,plaintext,key,dim):
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


    def decrypt(self,ciphertext,key,dim):
        k_m = key_matrix(key, dim)
        #decryption not possible
        if (deter(k_m) == 0 or deter(k_m) == 13 or deter(k_m) % 2 == 0):
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



#Columnar transposition cipher
class Columnar:
    def __init__(self):pass


    def encrypt(self,plaintext,key):
        plaintext = plaintext.replace(" ", "")
        rows = math.ceil(len(plaintext)/len(key))
        position = 0
        m = []
        for i in range(rows):
            r = []
            for j in range(len(key)):
                if(position < len(plaintext)):
                    r.append(plaintext[position])
                else:
                    r.append("a")
                position += 1
            m.append(r)
        b = ""
        for i in range(1, len(key)+1):
            for j in range(rows):
                index = key.find(str(i))
                b += m[j][index]
        return b


    def decrypt(self,ciphertext,key):
        ciphertext = ciphertext.replace(" ", "")
        rows = math.ceil(len(ciphertext)/len(key))
        position = 0
        m = []
        for i in range(len(key)):
            r = []
            for j in range(rows):
                if(position < len(ciphertext)):
                    r.append(ciphertext[position])
                else:
                    r.append("a")
                position += 1
            m.append(r)
        rev_key = ""
        for i in range(1, len(key)+1):
            rev_key += str(key.find(str(i))+1)
        b = [["" for i in range(len(rev_key))] for j in range(rows)]
        for i in range(rows):
            for j in range(len(rev_key)):
                b[i][j] = m[j][i]
        b_s = [["" for i in range(len(rev_key))] for j in range(rows)]
        for i in range(1, len(key)+1):
            for j in range(rows):
                index = rev_key.find(str(i))
                b_s[j][i-1] = b[j][index]
        plaintext = ""
        for i in b_s:
            plaintext += "".join(i)
        return plaintext



#Railfence
class Railfence:
    def __init__(self):pass


    def encrypt(self,text,key):
        rail = [['\n' for i in range(len(text))] for j in range(key)]
        dir_down = False
        row, col = 0, 0
        for i in range(len(text)): 
            # check the direction of flow 
            # reverse the direction if we've just 
            # filled the top or bottom rail 
            if (row == 0) or (row == key - 1): 
                dir_down = not dir_down 
            
            # fill the corresponding alphabet 
            rail[row][col] = text[i] 
            col += 1
            
            # find the next row using 
            # direction flag 
            if dir_down: 
                row += 1
            else: 
                row -= 1
        # now we can construct the cipher  
        # using the rail matrix 
        result = []
        for i in range(key): 
            for j in range(len(text)): 
                if rail[i][j] != '\n': 
                    result.append(rail[i][j]) 
        return("" . join(result))


    def decrypt(self,cipher,key):
        rail = [['\n' for i in range(len(cipher))] for j in range(key)] 
        # to find the direction 
        dir_down = None
        row, col = 0, 0
        # mark the places with '*' 
        for i in range(len(cipher)): 
            if row == 0: 
                dir_down = True
            if row == key - 1: 
                dir_down = False
            # place the marker 
            rail[row][col] = '*'
            col += 1
            
            # find the next row  
            # using direction flag 
            if dir_down: 
                row += 1
            else: 
                row -= 1
        # now we can construct the  
        # fill the rail matrix 
        index = 0
        for i in range(key): 
            for j in range(len(cipher)): 
                if ((rail[i][j] == '*') and
                (index < len(cipher))): 
                    rail[i][j] = cipher[index] 
                    index += 1
        # now read the matrix in  
        # zig-zag manner to construct 
        # the resultant text 
        result = [] 
        row, col = 0, 0
        for i in range(len(cipher)): 
            # check the direction of flow 
            if row == 0: 
                dir_down = True
            if row == key-1: 
                dir_down = False
            # place the marker 
            if (rail[row][col] != '*'): 
                result.append(rail[row][col]) 
                col += 1
            # find the next row using 
            # direction flag 
            if dir_down: 
                row += 1
            else: 
                row -= 1
        return("".join(result))