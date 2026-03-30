#Fernet algorithme dechiffrement symetrique
from cryptography.fernet import Fernet

message_clair="Bonjour Blessing "

cle_de_chiffrement=Fernet.generate_key()

chiffrement=Fernet(cle_de_chiffrement)
message_chiffre=chiffrement.encrypt(message_clair.encode())
print(f"messageclaire:{message_clair}")
print(f"messagechiffre:{message_chiffre}")