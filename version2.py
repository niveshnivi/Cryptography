#!/usr/bin/env python
#A file that imports the python module encrypt from Version1 and uses files to input and output Data
import version1
from version1 import encrypt
letter_key = ['a', 'd', 'f', 'g', 'v', 'x']
lpha_key = [ ['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p', 'q', 'r'], ['s', 't', 'u', 'v', 'w', 'x'], ['y', 'z', '0', '1', '2', '3'], ['4', '5', '6', '7', '8', '9'] ]
step1 = {}
Matrix = []
FinalHash = {}
rebuild = {}
plaintext = open("plaintext.txt","r+");
key = open("secretkey.txt","r+")
cipherfile = open("ciphertext.txt","a")

text_list = plaintext.read().splitlines()
key_list = key.read().splitlines()

for i in range(0,len(text_list)):
    text2 = text_list[i].replace(" ","")
    secret = key_list[i]
    #print(encrypt(text2, secret))
    cipherfile.write("the cipher text for " + text2 + " is " + encrypt(text2,secret) + "\n")
    print("written the cipher texts to the file... Check it out")
plaintext.close()
key.close()
cipherfile.close()