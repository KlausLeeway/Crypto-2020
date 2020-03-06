# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""



import os

#print(ord("c"))
#print(chr(90))

def decaler(caractere, decalage):
    a = ord(caractere)
    b = chr(a+decalage)
    
    return b
    

#print(decaler("a",3))


def chiffrement_cesar(message, clé):
    
    Nmessage = list(message)
    a = []    
    for i in Nmessage:
        a.append(decaler(i,clé))    
    a = "".join(a)            
    return a

#print(chiffrement_cesar("bonjour", 3))

def dechiffrement_cesar(message, clé):
    Nmessage = list(message)
    a = []    
    for i in Nmessage:
        a.append(decaler(i,-clé))    
    a = "".join(a)            
    return a


#print(dechiffrement_cesar("erqmrxu", 3))



with open('message2.txt', 'r' , encoding = 'utf8') as file:
    # on fait des choses avec le fichier
    message2 = file.read() # chaîne de caractère avec le contenu du fichier
    # bla
# à partir d'ici, le fichier est fermé
    
#print(message)
    
print(dechiffrement_cesar(message2, 8))


with open('message3.txt', 'r' , encoding = 'utf8') as file:
    message3 = file.read()
    
print(message3)
    
    
    
    

    
    
    