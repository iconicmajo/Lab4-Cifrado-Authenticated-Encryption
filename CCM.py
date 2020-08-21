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

#codigo referenciado y extraido de: https://gist.github.com/jbdatko/7425443


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
#El header autentica el mensaje, es decir garantiza que lo que recibe Bob fue el mensaje que envio Alice
hdr = b'Este es un header'
#el texto plano a encriptar (Mensaje)
plaintext = b'Legend has it that there was an evil and quarrelsome character named Jack the Stingy. The devil got the rumor about this Jack and went to see if he was indeed as evil as they said.'
#la llave ingresada
key = b'CC3078CC3078CC30'
#se genera un vector inicial de forma random
nonce = get_random_bytes(11)
#Se llama a la libreria de AES y se le pasan como parametros la llave, el modo que deseamos y el vector inicial
cipher = AES.new(key, AES.MODE_CCM, nonce)
#se actualiza el header dentro del cipher
cipher.update(hdr)
#A la variable de mensaje se le pasa tanto el vector, el header,
#  el texto encriptado (llamando a la funcion encrypt) 
# y la funcion cipher.digest() crea el MAC
msg = nonce, hdr, cipher.encrypt(plaintext), cipher.digest()
# Muestra el mensaje encriptado
print('\nEl mensaje encriptado es: \n',msg, '\n')

#************************************************
#               DESENCRIPCION
#************************************************

# Se asume que el mensaje a recibir de Alice tendra la siguiente estructura:

#tendra el vector, header para autenticar, el texto cifrado y el mac generado
nonce, hdr, ciphertext, mac = msg
#Se llama a la funcion de la libreria que recibe como parametros la llave, el modo de AES utilizado y el vector
cipher = AES.new(key, AES.MODE_CCM, nonce)
#Se hace un uptade al header para comprobar la autenticidad del texto
cipher.update(hdr)
#Se desencripta el texto con la funcion decrypt
plaintext = cipher.decrypt(ciphertext)
try:
    #Se intenta verificar que el mac sea valido, que el mensaje sea cifrado con la llave correcta y no haya sufrido modificaciones
    cipher.verify(mac) 
    print ('\n',"El mensaje fue autenticado:\n El header es: %s,\n El texto descifrado es: %s \n" % (hdr, plaintext))
except ValueError:
    #En caso de error solo le decimos al atacante que fallo 
    print ("Intenta de nuevo, algo fallo e hizo CATAPLOSH")