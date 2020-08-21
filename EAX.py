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

#codigo referenciado y extraido de: https://nitratine.net/blog/post/python-encryption-and-decryption-with-pycryptodome/#eax-example


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#Informacion a utilizar el texto y llave
data = b'Legend has it that there was an evil and quarrelsome character named Jack the Stingy. The devil got the rumor about this Jack and went to see if he was indeed as evil as they said.'
key = b'CC3078CC3078CC30'

#Se llama a la funcion de la libreria con el modo a utilizar de AES y la llave
cipher = AES.new(key, AES.MODE_EAX) 
#aqui se encripta la el texto y genera el tag
ciphered_data, tag = cipher.encrypt_and_digest(data) 
#aqui generamos aleatoriamente el vector de forma random
#aqui creamos un vector random, es el autogenerado por la libreria de forma automatica
nonce =cipher.nonce
#Se imprimen los datos 
print('\nEl vector inicial es: ',nonce,'\n')
print('\nEl texto encriptado es:\n ',ciphered_data,'\n\n')
print('\nEl tag generado es: ',tag,'\n')

#************************************************
#               DESENCRIPCION
#************************************************

# Se llama a la funcion de AES con la llave, el modo y el vector inicial
cipher = AES.new(key, AES.MODE_EAX, nonce)
#Aqui haceos el desencripcion y se verifica que el tag sea valido
original_data = cipher.decrypt_and_verify(ciphered_data, tag) 
print('\nEl texto desenciptado es: \n', original_data,'\n')