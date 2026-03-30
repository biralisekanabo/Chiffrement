#Fernet algorithme dechiffrement symetrique
from cryptography.fernet import Fernet
import mysql.connector
import os

def connecter():
bd=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    database="securite"
) 

return curseur 
def chiffrer(val_message_clair):
    cle=os.environ.get("Fernet")
    chiffrement=Fernet(cle.encode)
    message_chiffre=chiffrement.encrypt(val_message_clair.encode())
    return message_chiffre

def enregistrer_utilisateur():

    pass

print(chiffrer("Bonjour tout le monde"))
#message_clair="Bonjour Blessing "

#cle_de_chiffrement=Fernet.generate_key()

#chiffrement=Fernet(cle_de_chiffrement)
#message_chiffre=chiffrement.encrypt(message_clair.encode())
#print(f"message clair:{message_clair}")
#print(f"messagechiffre:{message_chiffre}")
#message_dechiffre= chiffrement.decrypt(message_chiffre).decode()
#print(f"message dechiffre:{message_dechiffre}")