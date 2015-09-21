#!/usr/bin/env python
#A python code that is used to encrypt and decrypt data based on ADFGVX cipher and takes input from the user

letter_key = ['a', 'd', 'f', 'g', 'v', 'x']
alpha_key = [ ['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p', 'q', 'r'], ['s', 't', 'u', 'v', 'w', 'x'], ['y', 'z', '0', '1', '2', '3'], ['4', '5', '6', '7', '8', '9'] ]
step1 = {}
Matrix = []
FinalHash = {}
rebuild = {}
 


def build(plainText):
    buildString = ""
    for letter in plainText:
        buildString = buildString + step1[letter]
    return(buildString)
      
def transpose(data,secretKey):
    length = len(secretKey)
    for n in range(0,len(data)-1,length):
        Matrix.append(list(data[n:n+(length)]))

def sortMatrix(secretKey,rowcount):
    str=""
    for i in range(len(secretKey)):
        for j in range(rowcount):
             str = str + Matrix[j][i]
        FinalHash[secretKey[i]] = str  
        str = "" 
   
def encrypt(plainText,secretKey):
    cipherText = ""
    for letter in plainText:
       substitute(letter)
    built = build(plainText)
    #data = str(secretKey) + built
    data = built
    transpose(data,secretKey)
    rowcount = int(len(data)/len(secretKey))
    sortMatrix(secretKey,rowcount)   
    for key in sorted(FinalHash):
        cipherText += FinalHash[key]
    return(cipherText)

def substitute(letter):
    step2 = {}
    for i in range(6):
        for j in range(6):
            if(alpha_key[i][j] == letter):
                letter1 = letter_key[i]
                letter2 = letter_key[j]
                merged = letter1 + letter2
                step1[letter] = merged

def decrypt(cipher,secretKey):
    sortSecretKey = sorted(secretKey)
    lenKey = len(sortSecretKey)
    lenCipher = len(cipher)
    calLen = int(lenCipher/lenKey)
    build = ""
    plaintext = ""
    set = 0;
    for i in range(0,lenKey):
        rebuild[sortSecretKey[i]] = cipher[set:set+calLen]
        set = set+calLen
    for i in range(0,calLen):
        for j in secretKey:
            build = build + rebuild[j][i]
    for i in range(0,len(build),2):
        matrix = build[i:i+2]
        row = letter_key.index(matrix[0])
        column = letter_key.index(matrix[1])
        plaintext = plaintext + alpha_key[row][column]
    return(plaintext)   

if __name__ == '__main__':
    
    while(input("Continue(c) or Quit(Q)") != "Q"):
        choice = input("Do you want to encrypt or decrypt")
        if(choice == "encrypt"):
            plainText = input("give the input plain text to encrypt").replace(" ","")
            secretKey = input("enter the secret key")
            print("*********************")  
            print("The plain Text to encode is " + plainText)
            print("*********************")    
            print("The encrypted cipher Text is " + encrypt(plainText,secretKey))
            print("*********************") 
        elif(choice == "decrypt"):
            cipher = input("Enter the cipher text you want to decode")
            secretKey2 = input("Input the secret key you want to use to decrypt it")
            print("*********************")  
            print("The cipher text to decode is " + cipher)
            print("*********************")
            print("The original plain text is " + decrypt(cipher,secretKey2))
            print("*********************") 
    

