import binascii
from cryptography.fernet import Fernet
from secretsharing import SecretSharer
import requests

sentence = "My name is Adrian."
key = Fernet.generate_key()
cipher_suite = Fernet(key)
ciphertext = cipher_suite.encrypt(sentence.encode())

hex_key = binascii.hexlify(key).decode()

shares = SecretSharer.split_secret(hex_key, 3, 5)

share_to_paste = shares[0]
paste_content = f"Ciphertext: {ciphertext.decode()}\nShare: {share_to_paste}"

url = "https://api.paste.ee/v1/pastes"
headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": "aDMZT7E9A9BgNtTRulDvDEG5YsgjvFklj8DzuC2os"
}
data = {
    "description": "Shamir Secret Sharing Example",
    "sections": [{"name": "Secret", "syntax": "text", "contents": paste_content}],
    "expire": "6m"
}
response = requests.post(url, json=data, headers=headers)

if response.status_code == 201:
    paste_url = response.json().get("link")
    print(f"Paste URL: {paste_url}")
else:
    print(f"Failed to upload to paste.ee: {response.text}")

print(f"Share verslag: {shares[1]}")
