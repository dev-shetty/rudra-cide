from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import base64

from config import KEY

def encrypt(text):
    derived_key = PBKDF2(KEY, b'salt', dkLen=32, count=1000)
    cipher = AES.new(derived_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(text.encode('utf-8'))
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')

def decrypt(ciphertext):
    derived_key = PBKDF2(KEY, b'salt', dkLen=32, count=1000)
    data = base64.b64decode(ciphertext.encode('utf-8'))
    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]
    cipher = AES.new(derived_key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode('utf-8')
