from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

def derive_key(secret: bytes, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32, 
        salt=salt,
        iterations=100000,
    )
    return kdf.derive(secret)

secret = b'my_shared_secret_passphrase'
salt = os.urandom(16)

key = derive_key(secret, salt)

print(f"Derived AES key (256-bit) using SHA-512: {key.hex()}")

message = b"Hi my name is Adrian."

iv = os.urandom(12)

cipher = Cipher(algorithms.AES(key), modes.GCM(iv))
encryptor = cipher.encryptor()
ciphertext = encryptor.update(message) + encryptor.finalize()

auth_tag = encryptor.tag

print(f"\nCiphertext: {ciphertext.hex()}")
print(f"IV: {iv.hex()}")
print(f"Auth Tag: {auth_tag.hex()}")

cipher = Cipher(algorithms.AES(key), modes.GCM(iv, auth_tag))
decryptor = cipher.decryptor()
decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()

print(f"\nDecrypted message: {decrypted_message.decode()}")
