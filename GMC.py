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
#codigo referenciado y extraido de: https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/symmetric-key-ciphers/aes-encrypt-decrypt-examples.html

#Implemtnacion GCM (parte2.1)
from Crypto.Cipher import AES
import binascii, os

#funcion de enccripcion
def encrypt_AES_GCM(msg, secretKey):
  #Llamando a la libreria de AES, le pasamos la llave y mecionamos el modo AES que queremos
    aesCipher = AES.new(secretKey, AES.MODE_GCM) 
    #Tomando la llave generada anteriormente se llama a la funcion encrypt_and_digest de la libreria y se le pasa
    #como parametro el mensaje para que este sea procesado y encriptado
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg) 
    #regresa el texto encriptado, el vector inicial generado de manera y el Tag
    return (ciphertext, aesCipher.nonce, authTag)

#Funcion para desencripcion (a texto legible)
def decrypt_AES_GCM(encryptedMsg, secretKey):
    #Se separa en 3 partes todo el mensaje, desde el texto, el vector y el tag
    (ciphertext, nonce, authTag) = encryptedMsg 
    #De nuevo se llama a la libreria y ahora se le pasa 3 parametros, indiciando la llave, el modo del AES que se usa
    #Y tambien el vector inicial
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    #Este llama la funcion que desencripta y verifica que el tag sea el correcto
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    #regresa el texto ya legible
    return plaintext

secretKey = os.urandom(32)  # 256-bit llave random generada 
print("Llave de encripcion:", binascii.hexlify(secretKey))
#Este es el mensaje 
cleartext = b'Legend has it that there was an evil and quarrelsome character named Jack the Stingy. The devil got the rumor about this Jack and went to see if he was indeed as evil as they said.'
#aqui recie el mensaje y la llave como parametros nuestra func
encryptedMsg = encrypt_AES_GCM(cleartext, secretKey)

#aqui hace el print del mensaje encriptado
print('\n\n',"Parte del Mensaje Encriptado",'\n\n', 
    'Texto Encriptado: ', binascii.hexlify(encryptedMsg[0]),'\n\n',#Texto encriptado
    'Vector Inicial: ', binascii.hexlify(encryptedMsg[1]),'\n\n', #Vector inicial
    'TAG: ', binascii.hexlify(encryptedMsg[2]),'\n\n' #Tag utilizado para el MAC
)

#************************************************
#               DESENCRIPCION
#************************************************

decryptedMsg = decrypt_AES_GCM(encryptedMsg, secretKey)
#aqui imprimimos el mensaje encriptado
print('Mensaje desencriptado: ',decryptedMsg, '\n\n',)
