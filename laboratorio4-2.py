
"""
Laboratorio 4
Cifrado de información
#Maria Jose Castro 181202
#Diana de Leon 18607
#Camila Gonzalez 18398
#Maria Ines Vasquez 18250
#Christopher Barrios 18207
#Jose Garavito 18071
"""

#Argon2
#Extraído de https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html
#Install
#pip install passlib
#pip install argon2_cffi
from passlib.hash import argon2

# genera nuevo salt, dado que no lo mandamos nosotros crea uno default, y generar contraseña "hasheada"
#esta función puede recibir una gran cantidad de parámetros como cantidad de rondsas, costo de memoria, entre otros, pero si no se especifica utiliza los valores default
h = argon2.hash("password")
#adentro de la función, la variable sprint que se manda como input se codifica a UTF-8 y luego es mandado a la función Argon2 para hacerle hash
print(h)
print(argon2.verify("password", h))
print(argon2.verify("contraseñaS", h))

#PBKDF2 
#Extraído de https://cryptobook.nakov.com/mac-and-key-derivation/pbkdf2
#Install
#pip install backports.pbkdf2
import os, binascii
from backports.pbkdf2 import pbkdf2_hmac
#salt son bits aleatorios para una función derivadora de claves y así es capaz de hacer contraseñas has única
salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1') ##genera data binaria de un valor hexadecimal
#Salt ayuda a agregarle longitud a la contraseña y así hacerlo más dificil de descifrar por ataques
word="password" #palabra que se desea "hashear" para encriptarlo
passwd = word.encode("utf8")#regresa la versión codificada de un string
key = pbkdf2_hmac("sha256", passwd, salt, 50000, 32) #se aplica la funcíón con la cantidad de iteraciones, el tipo de hash deseado, la palabra encriptar, el salt, y la longitud del output
print("Derived key:", binascii.hexlify(key))#se recibe de binario a hexadecimal para el output final



#Literatura citada:
#https://crypto.stackexchange.com/questions/1776/can-you-help-me-understand-what-a-cryptographic-salt-is

