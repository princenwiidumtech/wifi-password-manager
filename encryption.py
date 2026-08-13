from cryptography.fernet import Fernet
import os

KEY_FOLDER = "keys"
KEY_FILE = os.path.join(KEY_FOLDER, "secret.key")  

def generate_key():
    if not os.path.exists(KEY_FOLDER):
        os.makedirs(KEY_FOLDER)
        
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
            
def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()
        
generate_key()
fernet = Fernet(load_key())

def encrypt_password(password):
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return fernet.decrypt(encrypted_password.encode()).decode()