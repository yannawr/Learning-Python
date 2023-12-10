from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode

key = b"This is the super secret key 123"
ciphered_data = "CIPHER IN BASE64"
ivBytes = bytes([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

cipher = AES.new(key, AES.MODE_CBC, iv=ivBytes)
original_data = unpad(cipher.decrypt(b64decode(ciphered_data)), AES.block_size)

plaintext = original_data.decode('utf-8')

print(plaintext)