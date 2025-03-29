import string
def encrypt(message,shift,alphabet):
    msg=""
    i=0
    a=len(message)
    for i in range(a):
        if message[i]==" ":
            msg=msg+" "
        else:
            for j in range(len(alphabet)):
                if message[i]==alphabet[j]:
                    new_j=(j+shift)%26
                    msg=msg+alphabet[new_j]
    print(f"Here's the encryptd result:{msg}")
def decrypt(message,shift,alphabet):
    msg=""
    i=0
    a=len(message)
    for i in range(a):
        if message[i]==" ":
            msg=msg+" "
        else:
            for j in range(len(alphabet)):
                if message[i]==alphabet[j]:
                    if (j-shift)>=0:
                        new_j=(j-shift)%26
                        msg=msg+alphabet[new_j]
                    else:
                        c=j-shift+26
                        new_j=c%26
                        msg=msg+alphabet[new_j]
    print(f"Here's the decryptd result:{msg}") 
alphabet = list(string.ascii_lowercase)
entry=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
y_n="yes"
while y_n=="yes":
    if entry=="encrypt":
        msg=input("Type your message:\n")
        sft=int(input("Type the shift number:\n"))
        encrypt(message=msg,shift=sft,alphabet=alphabet)
        y_n=input("Type 'yes' if you want to go again.Otherwise type 'no'\n")
        if y_n=="yes":
            entry=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
            continue
        else:
            break
    elif entry=="decrypt":
        msg=input("Type your message:\n")
        sft=int(input("Type the shift number:\n"))
        decrypt(message=msg,shift=sft,alphabet=alphabet)
        y_n=input("Type 'yes' if you want to go again.Otherwise type 'no'\n")
        if y_n=="yes":
            entry=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
            continue
        else:
            break
    else:
        print("OOPS! you entered wrong code")
        y_n=input("Type 'yes' if you want to go again.Otherwise type 'no'\n")
        if y_n=="yes":
            entry=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
            continue
        else:
            break
print("GoodBye!")
    
