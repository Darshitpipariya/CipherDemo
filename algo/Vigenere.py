lower_alpha = "abcdefghijklmnopqrstuvwxyz"
upper_alpha = lower_alpha.upper()

def encrypt(plaintext,key):
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

def decrypt(ciphertext,key):
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