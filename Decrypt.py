from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import sys

key = b'mysecretpassword'

with open(sys.argv[1], 'rb') as c_file:
    iv = c_file.read(16)
    ciphertext = c_file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)

    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

with open(sys.argv[1], 'wb') as c_file:
    c_file.write(plaintext)
