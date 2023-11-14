from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import sys

key = b'mysecretpassword'

cipher = AES.new(key, AES.MODE_CBC)

with open(sys.argv[1], 'rb') as my_file:
    plaintext = my_file.read()

ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

print(ciphertext)

with open(sys.argv[1], 'wb') as c_file:
    c_file.write(cipher.iv)
    c_file.write(ciphertext)