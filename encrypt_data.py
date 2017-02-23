# This script requires that the Cryptodome module is installed.
#
# http://pycryptodome.readthedocs.io/en/latest/src/installation.html
# "pip install pycryptodomex" is good enough for Python 3.6
#
# Keep in mind that if you use "pip install pycryptodome" without the
#     final "x", you will need to change every import from "Cryptodome"
#     to "Crypto".

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Hash import SHA256
import sys

DEBUG = True #If True, it will try to read the passwords and display them on screen

def main(argv):
	file = argv[0]
	key = bytes(argv[1], encoding='UTF-8')
	data = bytes(argv[2], encoding='UTF-8')

	cipher(file, key, data)

	global DEBUG
	if DEBUG:
		decipher(file, key)

def cipher(file, key, data):
	key = bytes(SHA256.new(key).hexdigest()[:16], encoding='UTF-8')
	cipher = AES.new(key, AES.MODE_EAX)
	ciphertext, tag = cipher.encrypt_and_digest(data)

	file_out = open(file, "wb")
	[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
	file_out.close()

def decipher(file, key):
	key = bytes(SHA256.new(key).hexdigest()[:16], encoding='UTF-8')
	file_in = open(file, "rb")
	nonce = file_in.read(16)
	tag = file_in.read(16)
	ciphertext = file_in.read()
	file_in.close()

	# let's assume that the key is somehow available again
	cipher2 = AES.new(key, AES.MODE_EAX, nonce)
	data = cipher2.decrypt_and_verify(ciphertext, tag)

	print("Data readed from file: "+str(data))


if __name__ == "__main__":
	if (len(sys.argv) <= 3 or len(sys.argv) > 4):
		print("Usage: "+sys.argv[0]+" [file] [password] [data]")
	else:
		main(sys.argv[1:])