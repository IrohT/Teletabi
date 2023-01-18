# ___________crypto könyvtár__________
from cryptography.fernet import Fernet

# _______________kulcs generálás és "mentés"________
'''
kulcs = Fernet.generate_key()
  
with open('filekulcs.key', 'wb') as filekulcs:
  filekulcs.write(kulcs)
'''
# -------------------------------------------------

# ______________kulcs beolvasás___________
with open('filekey.key', 'rb') as filekulcs:
    kulcs = filekulcs.read()
    
fernet_kulcs = Fernet(kulcs)
# --------------------------------------------------

# __________________file megnyitása(olvasásra)___________
with open("teszt.py","rb") as file:
    eredeti_code = file.read()
# -------------------------------------------------

# _______________________file megnyitása(írásra) & encyrpetlés_____________
encrypted_code = fernet_kulcs.encrypt(eredeti_code)

with open("teszt.py","wb") as file:
    file.write(encrypted_code)
# -------------------------------------------------
    
# ____________________file megnyitása(olvasásra)______________

with open("teszt.py","rb") as file:
    encryptelt_code = file.read()
# --------------------------------------------------

#____________________file megnyitása(írásra) & decryptelés______________
decrypted_code = fernet_kulcs.decrypt(encryptelt_code)

with open("teszt.py","wb") as file:
    file.write(decrypted_code)
# ---------------------------------------------------

