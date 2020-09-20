import tkinter as tk
from tkinter import ttk
from algo import Autokey as au
from algo import Columnar as co
from algo import Caesar as ca
from algo import Otp as ot
from algo import Playfair as pl
from algo import Railfence as ra
from algo import Vigenere as vi
from algo import Monoalphabetic as mo
from algo import Hill as hi
root = tk.Tk()
root.title("CipherDemo")
root.geometry("1000x900")
tabControl = ttk.Notebook(root)

Autokey = tk.Frame(tabControl)
Caesar = tk.Frame(tabControl)
Columnar= tk.Frame(tabControl)
Hill= tk.Frame(tabControl)
Monoalphabetic= tk.Frame(tabControl)
Otp = tk.Frame(tabControl)
Playfair = tk.Frame(tabControl)
Railfence= tk.Frame(tabControl)
Vigenere= tk.Frame(tabControl)
#Tab controls
tabControl.add(Autokey, text ='Autokey')
tabControl.add(Caesar, text ='Caesar')
tabControl.add(Columnar, text ='Columnar')
tabControl.add(Hill, text ='Hill')
tabControl.add(Monoalphabetic, text ='Monoalphabetic')
tabControl.add(Otp, text ='Otp')
tabControl.add(Playfair, text ='Playfair')
tabControl.add(Railfence, text ='Railfence')
tabControl.add(Vigenere, text ='Vigenere')
tabControl.pack(expand =0,fill='x')


#AUTOKEY
def Autokey_Encrypt_cm():
    Autokey_Output_Text.delete("1.0","end")
    msg=Autokey_Encrypt_Text.get("1.0","end").strip()
    key=Autokey_Encrypt_Key.get('1.0',"end").strip()
    ciphertext=au.encrypt(msg,key)
    output="Ciphertext : "+ciphertext[0]+"\nGenerated key : "+ciphertext[1]
    Autokey_Output_Text.insert('1.0',output)

def Autokey_Decrypt_cm():
    Autokey_Output_Text.delete("1.0", "end")
    msg=Autokey_Decrypt_Text.get("1.0","end").strip()
    key=Autokey_Decrypt_Key.get('1.0',"end").strip()
    plaintext=au.decrypt(msg,key)
    output="Plaintext : "+plaintext[0]+"\nGenerated key : "+plaintext[1]
    Autokey_Output_Text.insert("1.0",output)


Auto_Upper=tk.Frame(Autokey)

Autokey_title= tk.Label(Auto_Upper, text ='Autokey', font = "Arial 50")
Autokey_title.pack(pady=5)
Autokey_discription=tk.Message(Auto_Upper,
                               text='Autokey Cipher is a polyalphabetic substitution cipher. It is closely related to the Vigenere cipher but uses a different method of generating the key.In this cipher, the key is a stream of subkeys which is used to encrypt the corresponding character in the plaintext.'
                                ,font='verdana 14 italic',width=1000)
Autokey_discription.pack(pady=5)
Auto_Upper.pack()

Auto_Lower=tk.Frame(Autokey)

Autokey_Encrypt= tk.Label(Auto_Lower, text ='Encrypt', font = "Bold 30",anchor=tk.CENTER)
Autokey_Encrypt.grid(row=0,column=0,pady=20,padx=100,columnspan=2)
Autokey_Encrypt_Text_label = tk.Label(Auto_Lower, text = "Text",font='Bold 20')
Autokey_Encrypt_Text_label.grid(row=1,column=0,padx=30)
Autokey_Encrypt_Text = tk.Text(Auto_Lower, height = 10, width = 50)
Autokey_Encrypt_Text.grid(row=1,column=1)
Autokey_Encrypt_Key_label = tk.Label(Auto_Lower, text = "Key",font='Bold 20')
Autokey_Encrypt_Key_label.grid(row=2,column=0,pady=35)
Autokey_Encrypt_Key = tk.Text(Auto_Lower, height = 5, width = 50)
Autokey_Encrypt_Key.grid(row=2,column=1)
Autokey_Encrypt_Btn=tk.Button(Auto_Lower,text='Encrypt',font='Bold 12',command=Autokey_Encrypt_cm,height=2,width=10)
Autokey_Encrypt_Btn.grid(row=3,column=1,pady=5)

Autokey_Decrypt= tk.Label(Auto_Lower, text ='Decrypt', font = "Bold 30",anchor=tk.CENTER)
Autokey_Decrypt.grid(row=0,column=2,padx=100,columnspan=2)
Autokey_Decrypt_Text_label = tk.Label(Auto_Lower, text = "Text",font = "Bold 20")
Autokey_Decrypt_Text_label.grid(row=1,column=2,padx=30)
Autokey_Decrypt_Text = tk.Text(Auto_Lower, height = 10, width = 50)
Autokey_Decrypt_Text.grid(row=1,column=3)
Autokey_Decrypt_Key_label = tk.Label(Auto_Lower, text = "Key",font = "Bold 20")
Autokey_Decrypt_Key_label.grid(row=2,column=2)
Autokey_Decrypt_Key = tk.Text(Auto_Lower, height = 5, width = 50)
Autokey_Decrypt_Key.grid(row=2,column=3)
Autokey_Decrypt_Btn=tk.Button(Auto_Lower,text='Decrypt',font='Bold 12',command=Autokey_Decrypt_cm,height=2,width=10)
Autokey_Decrypt_Btn.grid(row=3,column=3)

Autokey_Output_label= tk.Label(Auto_Lower, text ='Output', font = "Bold 30")
Autokey_Output_label.grid(row=4,column=0,padx=10)
Autokey_Output_Text = tk.Text(Auto_Lower, height =15, width = 100)
Autokey_Output_Text.grid(row=4,column=1,columnspan=3,pady=10)
Auto_Lower.pack()


#Caesar
def Caesar_Encrypt_cm():
    Caesar_Output_Text.delete("1.0","end")
    msg=Caesar_Encrypt_Text.get("1.0","end").strip()
    key=Caesar_Encrypt_Key.get('1.0',"end").strip()
    ciphertext=ca.encrypt(msg,int(key))
    Caesar_Output_Text.insert('1.0',ciphertext)

def Caesar_Decrypt_cm():
    Caesar_Output_Text.delete("1.0", "end")
    msg=Caesar_Decrypt_Text.get("1.0","end").strip()
    key=Caesar_Decrypt_Key.get('1.0',"end").strip()
    plaintext=ca.decrypt(msg,int(key))
    Caesar_Output_Text.insert("1.0",plaintext)
Caesar_Upper = tk.Frame(Caesar)
Caesar_title = tk.Label(Caesar_Upper, text="Caesar", font="Arial 50")
Caesar_title.pack(pady=5)
Caesar_discription = tk.Message(
    Caesar_Upper,
    text="The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet.",
    font="verdana 14 italic",
    width=1000,
)
Caesar_discription.pack(pady=5)
Caesar_Upper.pack()


Caesar_Lower = tk.Frame(Caesar)

Caesar_Encrypt = tk.Label(
    Caesar_Lower, text="Encrypt", font="Bold 30", anchor=tk.CENTER
)
Caesar_Encrypt.grid(row=0, column=0, pady=20, padx=100, columnspan=2)
Caesar_Encrypt_Text_label = tk.Label(Caesar_Lower, text="Text", font="Bold 20")
Caesar_Encrypt_Text_label.grid(row=1, column=0, padx=30)
Caesar_Encrypt_Text = tk.Text(Caesar_Lower, height=10, width=50)
Caesar_Encrypt_Text.grid(row=1, column=1)
Caesar_Encrypt_Key_label = tk.Label(Caesar_Lower, text="Key", font="Bold 20")
Caesar_Encrypt_Key_label.grid(row=2, column=0, pady=35)
Caesar_Encrypt_Key = tk.Text(Caesar_Lower, height=5, width=50)
Caesar_Encrypt_Key.grid(row=2, column=1)
Caesar_Encrypt_Btn = tk.Button(
    Caesar_Lower, text="Encrypt", font="Bold 12", command=Caesar_Encrypt_cm, height=2, width=10
)
Caesar_Encrypt_Btn.grid(row=3, column=1, pady=5)

Caesar_Decrypt = tk.Label(
    Caesar_Lower, text="Decrypt", font="Bold 30", anchor=tk.CENTER
)
Caesar_Decrypt.grid(row=0, column=2, padx=100, columnspan=2)
Caesar_Decrypt_Text_label = tk.Label(Caesar_Lower, text="Text", font="Bold 20")
Caesar_Decrypt_Text_label.grid(row=1, column=2, padx=30)
Caesar_Decrypt_Text = tk.Text(Caesar_Lower, height=10, width=50)
Caesar_Decrypt_Text.grid(row=1, column=3)
Caesar_Decrypt_Key_label = tk.Label(Caesar_Lower, text="Key", font="Bold 20")
Caesar_Decrypt_Key_label.grid(row=2, column=2)
Caesar_Decrypt_Key = tk.Text(Caesar_Lower, height=5, width=50)
Caesar_Decrypt_Key.grid(row=2, column=3)
Caesar_Decrypt_Btn = tk.Button(
    Caesar_Lower, text="Decrypt", font="Bold 12", command=Caesar_Decrypt_cm, height=2, width=10
)
Caesar_Decrypt_Btn.grid(row=3, column=3)

Caesar_Output_label = tk.Label(Caesar_Lower, text="Output", font="Bold 30")
Caesar_Output_label.grid(row=4, column=0, padx=10)
Caesar_Output_Text = tk.Text(Caesar_Lower, height=15, width=100)
Caesar_Output_Text.grid(row=4, column=1, columnspan=3, pady=10)
Caesar_Lower.pack()



#Columnar
def Columnar_Encrypt_cm():
    Columnar_Output_Text.delete("1.0","end")
    msg=Columnar_Encrypt_Text.get("1.0","end").strip()
    key=Columnar_Encrypt_Key.get('1.0',"end").strip()
    ciphertext=co.encrypt(msg,key)
    Columnar_Output_Text.insert('1.0',ciphertext)

def Columnar_Decrypt_cm():
    Columnar_Output_Text.delete("1.0", "end")
    msg=Columnar_Decrypt_Text.get("1.0","end").strip()
    key=Columnar_Decrypt_Key.get('1.0',"end").strip()
    plaintext=co.decrypt(msg,key)
    Columnar_Output_Text.insert("1.0",plaintext)

Columnar_Upper = tk.Frame(Columnar)
Columnar_title = tk.Label(Columnar_Upper, text="Columnar", font="Arial 50")
Columnar_title.pack(pady=5)
Columnar_discription = tk.Message(
    Columnar_Upper,
    text="The Columnar Transposition Cipher is a form of transposition cipher just like Rail Fence Cipher. Columnar Transposition involves writing the plaintext out in rows, and then reading the ciphertext off in columns one by one.",
    font="verdana 14 italic",
    width=1000,
)
Columnar_discription.pack(pady=5)
Columnar_Upper.pack()


Columnar_Lower = tk.Frame(Columnar)

Columnar_Encrypt = tk.Label(
    Columnar_Lower, text="Encrypt", font="Bold 30", anchor=tk.CENTER
)
Columnar_Encrypt.grid(row=0, column=0, pady=20, padx=100, columnspan=2)
Columnar_Encrypt_Text_label = tk.Label(Columnar_Lower, text="Text", font="Bold 20")
Columnar_Encrypt_Text_label.grid(row=1, column=0, padx=30)
Columnar_Encrypt_Text = tk.Text(Columnar_Lower, height=10, width=50)
Columnar_Encrypt_Text.grid(row=1, column=1)
Columnar_Encrypt_Key_label = tk.Label(Columnar_Lower, text="Key", font="Bold 20")
Columnar_Encrypt_Key_label.grid(row=2, column=0, pady=35)
Columnar_Encrypt_Key = tk.Text(Columnar_Lower, height=5, width=50)
Columnar_Encrypt_Key.grid(row=2, column=1)
Columnar_Encrypt_Btn = tk.Button(
    Columnar_Lower, text="Encrypt", font="Bold 12", command=Columnar_Encrypt_cm, height=2, width=10
)
Columnar_Encrypt_Btn.grid(row=3, column=1, pady=5)


Columnar_Decrypt = tk.Label(
    Columnar_Lower, text="Decrypt", font="Bold 30", anchor=tk.CENTER
)
Columnar_Decrypt.grid(row=0, column=2, padx=100, columnspan=2)
Columnar_Decrypt_Text_label = tk.Label(Columnar_Lower, text="Text", font="Bold 20")
Columnar_Decrypt_Text_label.grid(row=1, column=2, padx=30)
Columnar_Decrypt_Text = tk.Text(Columnar_Lower, height=10, width=50)
Columnar_Decrypt_Text.grid(row=1, column=3)
Columnar_Decrypt_Key_label = tk.Label(Columnar_Lower, text="Key", font="Bold 20")
Columnar_Decrypt_Key_label.grid(row=2, column=2)
Columnar_Decrypt_Key = tk.Text(Columnar_Lower, height=5, width=50)
Columnar_Decrypt_Key.grid(row=2, column=3)
Columnar_Decrypt_Btn = tk.Button(
    Columnar_Lower, text="Decrypt", font="Bold 12", command=Columnar_Decrypt_cm, height=2, width=10
)
Columnar_Decrypt_Btn.grid(row=3, column=3)


Columnar_Output_label = tk.Label(Columnar_Lower, text="Output", font="Bold 30")
Columnar_Output_label.grid(row=4, column=0, padx=10)
Columnar_Output_Text = tk.Text(Columnar_Lower, height=15, width=100)
Columnar_Output_Text.grid(row=4, column=1, columnspan=3, pady=10)
Columnar_Lower.pack()


#Playfair
def Playfair_Encrypt_cm():
    Playfair_Output_Text.delete("1.0","end")
    msg=Playfair_Encrypt_Text.get("1.0","end").strip()
    key=Playfair_Encrypt_Key.get('1.0',"end").strip()
    ciphertext=pl.encrypt(msg,key)
    Playfair_Output_Text.insert('1.0',ciphertext)

def Playfair_Decrypt_cm():
    Playfair_Output_Text.delete("1.0", "end")
    msg=Playfair_Decrypt_Text.get("1.0","end").strip()
    key=Playfair_Decrypt_Key.get('1.0',"end").strip()
    plaintext=pl.decrypt(msg,key)
    Playfair_Output_Text.insert("1.0",plaintext)


Playfair_Upper = tk.Frame(Playfair)
Playfair_title = tk.Label(Playfair_Upper, text="Playfair", font="Arial 50")
Playfair_title.pack(pady=5)
Playfair_discription = tk.Message(
    Playfair_Upper,
    text="The Playfair cipher was the first practical digraph substitution cipher. The scheme was invented in 1854 by Charles Wheatstone but was named after Lord Playfair who promoted the use of the cipher. In playfair cipher unlike traditional cipher we encrypt a pair of alphabets(digraphs) instead of a single alphabet.",
    font="verdana 14 italic",
    width=1000,
)
Playfair_discription.pack(pady=5)
Playfair_Upper.pack()


Playfair_Lower = tk.Frame(Playfair)

Playfair_Encrypt = tk.Label(
    Playfair_Lower, text="Encrypt", font="Bold 30", anchor=tk.CENTER
)
Playfair_Encrypt.grid(row=0, column=0, pady=20, padx=100, columnspan=2)
Playfair_Encrypt_Text_label = tk.Label(Playfair_Lower, text="Text", font="Bold 20")
Playfair_Encrypt_Text_label.grid(row=1, column=0, padx=30)
Playfair_Encrypt_Text = tk.Text(Playfair_Lower, height=10, width=50)
Playfair_Encrypt_Text.grid(row=1, column=1)
Playfair_Encrypt_Key_label = tk.Label(Playfair_Lower, text="Key", font="Bold 20")
Playfair_Encrypt_Key_label.grid(row=2, column=0, pady=35)
Playfair_Encrypt_Key = tk.Text(Playfair_Lower, height=5, width=50)
Playfair_Encrypt_Key.grid(row=2, column=1)
Playfair_Encrypt_Btn = tk.Button(
    Playfair_Lower, text="Encrypt", font="Bold 12", command=Playfair_Encrypt_cm, height=2, width=10
)
Playfair_Encrypt_Btn.grid(row=3, column=1, pady=5)


Playfair_Decrypt = tk.Label(
    Playfair_Lower, text="Decrypt", font="Bold 30", anchor=tk.CENTER
)
Playfair_Decrypt.grid(row=0, column=2, padx=100, columnspan=2)
Playfair_Decrypt_Text_label = tk.Label(Playfair_Lower, text="Text", font="Bold 20")
Playfair_Decrypt_Text_label.grid(row=1, column=2, padx=30)
Playfair_Decrypt_Text = tk.Text(Playfair_Lower, height=10, width=50)
Playfair_Decrypt_Text.grid(row=1, column=3)
Playfair_Decrypt_Key_label = tk.Label(Playfair_Lower, text="Key", font="Bold 20")
Playfair_Decrypt_Key_label.grid(row=2, column=2)
Playfair_Decrypt_Key = tk.Text(Playfair_Lower, height=5, width=50)
Playfair_Decrypt_Key.grid(row=2, column=3)
Playfair_Decrypt_Btn = tk.Button(
    Playfair_Lower, text="Decrypt", font="Bold 12", command=Playfair_Decrypt_cm, height=2, width=10
)
Playfair_Decrypt_Btn.grid(row=3, column=3)


Playfair_Output_label = tk.Label(Playfair_Lower, text="Output", font="Bold 30")
Playfair_Output_label.grid(row=4, column=0, padx=10)
Playfair_Output_Text = tk.Text(Playfair_Lower, height=15, width=100)
Playfair_Output_Text.grid(row=4, column=1, columnspan=3, pady=10)
Playfair_Lower.pack()


#Railfence
def Railfence_Encrypt_cm():
    Railfence_Output_Text.delete("1.0","end")
    msg=Railfence_Encrypt_Text.get("1.0","end").strip()
    key=Railfence_Encrypt_Key.get('1.0',"end").strip()
    ciphertext=ra.encrypt(msg,int(key))
    Railfence_Output_Text.insert('1.0',ciphertext)

def Railfence_Decrypt_cm():
    Railfence_Output_Text.delete("1.0", "end")
    msg=Railfence_Decrypt_Text.get("1.0","end").strip()
    key=Railfence_Decrypt_Key.get('1.0',"end").strip()
    plaintext=ra.decrypt(msg,int(key))
    Railfence_Output_Text.insert("1.0",plaintext)

Railfence_Upper = tk.Frame(Railfence)
Railfence_title = tk.Label(Railfence_Upper, text="Railfence", font="Arial 50")
Railfence_title.pack(pady=5)
Railfence_discription = tk.Message(
    Railfence_Upper,
    text="The rail fence cipher (also called a zigzag cipher) is a form of transposition cipher. It derives its name from the way in which it is encoded",
    font="verdana 14 italic",
    width=1000,
)
Railfence_discription.pack(pady=5)
Railfence_Upper.pack()


Railfence_Lower = tk.Frame(Railfence)

Railfence_Encrypt = tk.Label(
    Railfence_Lower, text="Encrypt", font="Bold 30", anchor=tk.CENTER
)
Railfence_Encrypt.grid(row=0, column=0, pady=20, padx=100, columnspan=2)
Railfence_Encrypt_Text_label = tk.Label(Railfence_Lower, text="Text", font="Bold 20")
Railfence_Encrypt_Text_label.grid(row=1, column=0, padx=30)
Railfence_Encrypt_Text = tk.Text(Railfence_Lower, height=10, width=50)
Railfence_Encrypt_Text.grid(row=1, column=1)
Railfence_Encrypt_Key_label = tk.Label(Railfence_Lower, text="Key", font="Bold 20")
Railfence_Encrypt_Key_label.grid(row=2, column=0, pady=35)
Railfence_Encrypt_Key = tk.Text(Railfence_Lower, height=5, width=50)
Railfence_Encrypt_Key.grid(row=2, column=1)
Railfence_Encrypt_Btn = tk.Button(
    Railfence_Lower, text="Encrypt", font="Bold 12", command=Railfence_Encrypt_cm, height=2, width=10
)
Railfence_Encrypt_Btn.grid(row=3, column=1, pady=5)


Railfence_Decrypt = tk.Label(
    Railfence_Lower, text="Decrypt", font="Bold 30", anchor=tk.CENTER
)
Railfence_Decrypt.grid(row=0, column=2, padx=100, columnspan=2)
Railfence_Decrypt_Text_label = tk.Label(Railfence_Lower, text="Text", font="Bold 20")
Railfence_Decrypt_Text_label.grid(row=1, column=2, padx=30)
Railfence_Decrypt_Text = tk.Text(Railfence_Lower, height=10, width=50)
Railfence_Decrypt_Text.grid(row=1, column=3)
Railfence_Decrypt_Key_label = tk.Label(Railfence_Lower, text="Key", font="Bold 20")
Railfence_Decrypt_Key_label.grid(row=2, column=2)
Railfence_Decrypt_Key = tk.Text(Railfence_Lower, height=5, width=50)
Railfence_Decrypt_Key.grid(row=2, column=3)
Railfence_Decrypt_Btn = tk.Button(
    Railfence_Lower, text="Decrypt", font="Bold 12", command=Railfence_Decrypt_cm, height=2, width=10
)
Railfence_Decrypt_Btn.grid(row=3, column=3)


Railfence_Output_label = tk.Label(Railfence_Lower, text="Output", font="Bold 30")
Railfence_Output_label.grid(row=4, column=0, padx=10)
Railfence_Output_Text = tk.Text(Railfence_Lower, height=15, width=100)
Railfence_Output_Text.grid(row=4, column=1, columnspan=3, pady=10)
Railfence_Lower.pack()


#Vigenere
def Vigenere_Encrypt_cm():
    Vigenere_Output_Text.delete("1.0","end")
    msg=Vigenere_Encrypt_Text.get("1.0","end").strip()
    key=Vigenere_Encrypt_Key.get('1.0',"end").strip()
    ciphertext=vi.encrypt(msg,key)
    Vigenere_Output_Text.insert('1.0',ciphertext)

def Vigenere_Decrypt_cm():
    Vigenere_Output_Text.delete("1.0", "end")
    msg=Vigenere_Decrypt_Text.get("1.0","end").strip()
    key=Vigenere_Decrypt_Key.get('1.0',"end").strip()
    plaintext=vi.decrypt(msg,key)
    Vigenere_Output_Text.insert("1.0",plaintext)

Vigenere_Upper = tk.Frame(Vigenere)
Vigenere_title = tk.Label(Vigenere_Upper, text="Vigenere", font="Arial 50")
Vigenere_title.pack(pady=5)
Vigenere_discription = tk.Message(
    Vigenere_Upper,
    text="Vigenere Cipher is a method of encrypting alphabetic text. It uses a simple form of polyalphabetic substitution. A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets .The encryption of the original text is done using the Vigenère square or Vigenère table.",
    font="verdana 14 italic",
    width=1000,
)
Vigenere_discription.pack(pady=5)
Vigenere_Upper.pack()


Vigenere_Lower = tk.Frame(Vigenere)

Vigenere_Encrypt = tk.Label(
    Vigenere_Lower, text="Encrypt", font="Bold 30", anchor=tk.CENTER
)
Vigenere_Encrypt.grid(row=0, column=0, pady=20, padx=100, columnspan=2)
Vigenere_Encrypt_Text_label = tk.Label(Vigenere_Lower, text="Text", font="Bold 20")
Vigenere_Encrypt_Text_label.grid(row=1, column=0, padx=30)
Vigenere_Encrypt_Text = tk.Text(Vigenere_Lower, height=10, width=50)
Vigenere_Encrypt_Text.grid(row=1, column=1)
Vigenere_Encrypt_Key_label = tk.Label(Vigenere_Lower, text="Key", font="Bold 20")
Vigenere_Encrypt_Key_label.grid(row=2, column=0, pady=35)
Vigenere_Encrypt_Key = tk.Text(Vigenere_Lower, height=5, width=50)
Vigenere_Encrypt_Key.grid(row=2, column=1)
Vigenere_Encrypt_Btn = tk.Button(
    Vigenere_Lower, text="Encrypt", font="Bold 12", command=Vigenere_Encrypt_cm, height=2, width=10
)
Vigenere_Encrypt_Btn.grid(row=3, column=1, pady=5)


Vigenere_Decrypt = tk.Label(
    Vigenere_Lower, text="Decrypt", font="Bold 30", anchor=tk.CENTER
)
Vigenere_Decrypt.grid(row=0, column=2, padx=100, columnspan=2)
Vigenere_Decrypt_Text_label = tk.Label(Vigenere_Lower, text="Text", font="Bold 20")
Vigenere_Decrypt_Text_label.grid(row=1, column=2, padx=30)
Vigenere_Decrypt_Text = tk.Text(Vigenere_Lower, height=10, width=50)
Vigenere_Decrypt_Text.grid(row=1, column=3)
Vigenere_Decrypt_Key_label = tk.Label(Vigenere_Lower, text="Key", font="Bold 20")
Vigenere_Decrypt_Key_label.grid(row=2, column=2)
Vigenere_Decrypt_Key = tk.Text(Vigenere_Lower, height=5, width=50)
Vigenere_Decrypt_Key.grid(row=2, column=3)
Vigenere_Decrypt_Btn = tk.Button(
    Vigenere_Lower, text="Decrypt", font="Bold 12", command=Vigenere_Decrypt_cm, height=2, width=10
)
Vigenere_Decrypt_Btn.grid(row=3, column=3)


Vigenere_Output_label = tk.Label(Vigenere_Lower, text="Output", font="Bold 30")
Vigenere_Output_label.grid(row=4, column=0, padx=10)
Vigenere_Output_Text = tk.Text(Vigenere_Lower, height=15, width=100)
Vigenere_Output_Text.grid(row=4, column=1, columnspan=3, pady=10)
Vigenere_Lower.pack()


#Otp
def Otp_Encrypt_cm():
    Otp_Output_Text.delete("1.0","end")
    msg=Otp_Encrypt_Text.get("1.0","end").strip()
    key=Otp_Encrypt_Key.get('1.0',"end").strip()
    ciphertext=ot.encrypt(msg,key)
    Otp_Output_Text.insert('1.0',ciphertext)

def Otp_Decrypt_cm():
    Otp_Output_Text.delete("1.0", "end")
    msg=Otp_Decrypt_Text.get("1.0","end").strip()
    key=Otp_Decrypt_Key.get('1.0',"end").strip()
    plaintext=ot.decrypt(msg,key)
    Otp_Output_Text.insert("1.0",plaintext)

Otp_Upper = tk.Frame(Otp)
Otp_title = tk.Label(Otp_Upper, text="Otp", font="Arial 50")
Otp_title.pack(pady=5)
Otp_discription = tk.Message(
    Otp_Upper,
    text="One-time pad cipher is a type of Vignere cipher which includes the following features \n−It is an unbreakable cipher.\n-The key is exactly same as the length of message which is encrypted.\n-The key is made up of random symbols.\n-As the name suggests, key is used one time only and never used again for any other message to be encrypted.",
    font="verdana 14 italic",
    width=1000,
)
Otp_discription.pack(pady=5)
Otp_Upper.pack()


Otp_Lower = tk.Frame(Otp)

Otp_Encrypt = tk.Label(
    Otp_Lower, text="Encrypt", font="Bold 30", anchor=tk.CENTER
)
Otp_Encrypt.grid(row=0, column=0, pady=20, padx=100, columnspan=2)
Otp_Encrypt_Text_label = tk.Label(Otp_Lower, text="Text", font="Bold 20")
Otp_Encrypt_Text_label.grid(row=1, column=0, padx=30)
Otp_Encrypt_Text = tk.Text(Otp_Lower, height=10, width=50)
Otp_Encrypt_Text.grid(row=1, column=1)
Otp_Encrypt_Key_label = tk.Label(Otp_Lower, text="Key", font="Bold 20")
Otp_Encrypt_Key_label.grid(row=2, column=0, pady=35)
Otp_Encrypt_Key = tk.Text(Otp_Lower, height=5, width=50)
Otp_Encrypt_Key.grid(row=2, column=1)
Otp_Encrypt_Btn = tk.Button(
    Otp_Lower, text="Encrypt", font="Bold 12", command=Otp_Encrypt_cm, height=2, width=10
)
Otp_Encrypt_Btn.grid(row=3, column=1, pady=5)


Otp_Decrypt = tk.Label(
    Otp_Lower, text="Decrypt", font="Bold 30", anchor=tk.CENTER
)
Otp_Decrypt.grid(row=0, column=2, padx=100, columnspan=2)
Otp_Decrypt_Text_label = tk.Label(Otp_Lower, text="Text", font="Bold 20")
Otp_Decrypt_Text_label.grid(row=1, column=2, padx=30)
Otp_Decrypt_Text = tk.Text(Otp_Lower, height=10, width=50)
Otp_Decrypt_Text.grid(row=1, column=3)
Otp_Decrypt_Key_label = tk.Label(Otp_Lower, text="Key", font="Bold 20")
Otp_Decrypt_Key_label.grid(row=2, column=2)
Otp_Decrypt_Key = tk.Text(Otp_Lower, height=5, width=50)
Otp_Decrypt_Key.grid(row=2, column=3)
Otp_Decrypt_Btn = tk.Button(
    Otp_Lower, text="Decrypt", font="Bold 12", command=Otp_Decrypt_cm, height=2, width=10
)
Otp_Decrypt_Btn.grid(row=3, column=3)


Otp_Output_label = tk.Label(Otp_Lower, text="Output", font="Bold 30")
Otp_Output_label.grid(row=4, column=0, padx=10)
Otp_Output_Text = tk.Text(Otp_Lower, height=15, width=100)
Otp_Output_Text.grid(row=4, column=1, columnspan=3, pady=10)
Otp_Lower.pack()


#Monoalphabetic
def Monoalphabetic_Encrypt_cm():
    Monoalphabetic_Output_Text.delete("1.0","end")
    msg=Monoalphabetic_Encrypt_Text.get("1.0","end").strip()
    ciphertext=mo.encrypt(msg)
    Monoalphabetic_Output_Text.insert('1.0',ciphertext)

def Monoalphabetic_Decrypt_cm():
    Monoalphabetic_Output_Text.delete("1.0", "end")
    msg=Monoalphabetic_Decrypt_Text.get("1.0","end").strip()
    plaintext=mo.decrypt(msg)
    Monoalphabetic_Output_Text.insert("1.0",plaintext)


Monoalphabetic_Upper = tk.Frame(Monoalphabetic)
Monoalphabetic_title = tk.Label(Monoalphabetic_Upper, text="Monoalphabetic", font="Arial 50")
Monoalphabetic_title.pack(pady=5)
Monoalphabetic_discription = tk.Message(
    Monoalphabetic_Upper,
    text="A monoalphabetic cipher is any cipher in which the letters of the plain text are mapped to cipher text letters based on a single alphabetic key. Examples of monoalphabetic ciphers would include the Caesar-shift cipher, where each letter is shifted based on a numeric key, and the atbash cipher, where each letter is mapped to the letter symmetric to it about the center of the alphabet.",
    font="verdana 14 italic",
    width=1000,
)
Monoalphabetic_discription.pack(pady=5)
Monoalphabetic_Upper.pack()


Monoalphabetic_Lower = tk.Frame(Monoalphabetic)

Monoalphabetic_Encrypt = tk.Label(
    Monoalphabetic_Lower, text="Encrypt", font="Bold 30", anchor=tk.CENTER
)
Monoalphabetic_Encrypt.grid(row=0, column=0, pady=20, padx=100, columnspan=2)
Monoalphabetic_Encrypt_Text_label = tk.Label(Monoalphabetic_Lower, text="Text", font="Bold 20")
Monoalphabetic_Encrypt_Text_label.grid(row=1, column=0, padx=30)
Monoalphabetic_Encrypt_Text = tk.Text(Monoalphabetic_Lower, height=10, width=50)
Monoalphabetic_Encrypt_Text.grid(row=1, column=1)
Monoalphabetic_Encrypt_Btn = tk.Button(
    Monoalphabetic_Lower, text="Encrypt", font="Bold 12", command=Monoalphabetic_Encrypt_cm, height=2, width=10
)
Monoalphabetic_Encrypt_Btn.grid(row=3, column=1, pady=5)


Monoalphabetic_Decrypt = tk.Label(
    Monoalphabetic_Lower, text="Decrypt", font="Bold 30", anchor=tk.CENTER
)
Monoalphabetic_Decrypt.grid(row=0, column=2, padx=100, columnspan=2)
Monoalphabetic_Decrypt_Text_label = tk.Label(Monoalphabetic_Lower, text="Text", font="Bold 20")
Monoalphabetic_Decrypt_Text_label.grid(row=1, column=2, padx=30)
Monoalphabetic_Decrypt_Text = tk.Text(Monoalphabetic_Lower, height=10, width=50)
Monoalphabetic_Decrypt_Text.grid(row=1, column=3)
Monoalphabetic_Decrypt_Btn = tk.Button(
    Monoalphabetic_Lower, text="Decrypt", font="Bold 12", command=Monoalphabetic_Decrypt_cm, height=2, width=10
)
Monoalphabetic_Decrypt_Btn.grid(row=3, column=3,pady=10)

Monoalphabetic_Output_label = tk.Label(Monoalphabetic_Lower, text="Output", font="Bold 30")
Monoalphabetic_Output_label.grid(row=4, column=0, padx=10)
Monoalphabetic_Output_Text = tk.Text(Monoalphabetic_Lower, height=15, width=100)
Monoalphabetic_Output_Text.grid(row=4, column=1, columnspan=3, pady=10)
Monoalphabetic_Lower.pack()


#Hill
def Hill_Encrypt_cm():
    Hill_Output_Text.delete("1.0","end")
    msg=Hill_Encrypt_Text.get("1.0","end").strip()
    key=Hill_Encrypt_Key.get('1.0',"end").strip()
    dim=Hill_Encrypt_Dim.get('1.0',"end").strip()
    ciphertext=hi.encrypt(msg,key,int(dim))
    Hill_Output_Text.insert('1.0',ciphertext)

def Hill_Decrypt_cm():
    Hill_Output_Text.delete("1.0", "end")
    msg=Hill_Decrypt_Text.get("1.0","end").strip()
    key=Hill_Decrypt_Key.get('1.0',"end").strip()
    dim=Hill_Decrypt_dim.get('1.0','end').strip()
    plaintext=hi.decrypt(msg,key,int(dim))
    Hill_Output_Text.insert("1.0",plaintext)

Hill_Upper = tk.Frame(Hill)
Hill_title = tk.Label(Hill_Upper, text="Hill", font="Arial 50")
Hill_title.pack(pady=5)
Hill_discription = tk.Message(
    Hill_Upper,
    text="Hill cipher is a polygraphic substitution cipher based on linear algebra.Each letter is represented by a number modulo 26. Often the simple scheme A = 0, B = 1, …, Z = 25 is used, but this is not an essential feature of the cipher. To encrypt a message, each block of n letters (considered as an n-component vector) is multiplied by an invertible n × n matrix, against modulus 26. To decrypt the message, each block is multiplied by the inverse of the matrix used for encryption",
    font="verdana 14 italic",
    width=1000,
)
Hill_discription.pack(pady=5)
Hill_Upper.pack()


Hill_Lower = tk.Frame(Hill)

Hill_Encrypt = tk.Label(
    Hill_Lower, text="Encrypt", font="Bold 30", anchor=tk.CENTER
)
Hill_Encrypt.grid(row=0, column=0, pady=20, padx=100, columnspan=2)
Hill_Encrypt_Text_label = tk.Label(Hill_Lower, text="Text", font="Bold 20")
Hill_Encrypt_Text_label.grid(row=1, column=0, padx=30)
Hill_Encrypt_Text = tk.Text(Hill_Lower, height=10, width=50)
Hill_Encrypt_Text.grid(row=1, column=1)
Hill_Encrypt_Key_label = tk.Label(Hill_Lower, text="Key", font="Bold 20")
Hill_Encrypt_Key_label.grid(row=2, column=0, pady=35)
Hill_Encrypt_Key = tk.Text(Hill_Lower, height=5, width=50)
Hill_Encrypt_Key.grid(row=2, column=1)
Hill_Encrypt_Dim_label = tk.Label(Hill_Lower, text="Dim", font="Bold 20")
Hill_Encrypt_Dim_label.grid(row=3, column=0, pady=10)
Hill_Encrypt_Dim = tk.Text(Hill_Lower, height=3, width=50)
Hill_Encrypt_Dim.grid(row=3, column=1)
Hill_Encrypt_Btn = tk.Button(
    Hill_Lower, text="Encrypt", font="Bold 12", command=Hill_Encrypt_cm, height=2, width=10
)
Hill_Encrypt_Btn.grid(row=4, column=1, pady=5)


Hill_Decrypt = tk.Label(
    Hill_Lower, text="Decrypt", font="Bold 30", anchor=tk.CENTER
)
Hill_Decrypt.grid(row=0, column=2, padx=100, columnspan=2)
Hill_Decrypt_Text_label = tk.Label(Hill_Lower, text="Text", font="Bold 20")
Hill_Decrypt_Text_label.grid(row=1, column=2, padx=30)
Hill_Decrypt_Text = tk.Text(Hill_Lower, height=10, width=50)
Hill_Decrypt_Text.grid(row=1, column=3)
Hill_Decrypt_Key_label = tk.Label(Hill_Lower, text="Key", font="Bold 20")
Hill_Decrypt_Key_label.grid(row=2, column=2)
Hill_Decrypt_Key = tk.Text(Hill_Lower, height=5, width=50)
Hill_Decrypt_Key.grid(row=2, column=3)
Hill_Decrypt_dim_label = tk.Label(Hill_Lower, text="Dim", font="Bold 20")
Hill_Decrypt_dim_label.grid(row=3, column=2)
Hill_Decrypt_dim = tk.Text(Hill_Lower, height=3, width=50)
Hill_Decrypt_dim.grid(row=3, column=3)
Hill_Decrypt_Btn = tk.Button(
    Hill_Lower, text="Decrypt", font="Bold 12", command=Hill_Decrypt_cm, height=2, width=10
)
Hill_Decrypt_Btn.grid(row=4, column=3)


Hill_Output_label = tk.Label(Hill_Lower, text="Output", font="Bold 30")
Hill_Output_label.grid(row=5, column=0, padx=10)
Hill_Output_Text = tk.Text(Hill_Lower, height=15, width=100)
Hill_Output_Text.grid(row=5, column=1, columnspan=3, pady=10)
Hill_Lower.pack()

root.mainloop()