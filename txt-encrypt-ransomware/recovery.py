#-*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
import os, sys, glob
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

## 1) Key Recovery (RSA decryption)
key_file_in = open("key.bin", "rb")
private_key = RSA.import_key(open("pkey/private.pem").read())
enc_key = key_file_in.read(private_key.size_in_bytes())
cipher_rsa = PKCS1_OAEP.new(private_key)
key = cipher_rsa.decrypt(enc_key)
print("key=",key)
key_file_in.close()
#key = b64encode(key).decode('utf-8')
# 그리고 나중에 key = b64decode(key of encryption)

## 2) File Recovery (AES decryption)
try:
    encFileObj = open("t1.enc", "rb")
    enc_data = encFileObj.read()
    encFileObj.close()
    print("enc_data=",enc_data)

    ivFileObj = open("iv/t1_iv.txt","rb")
    iv_data = b64decode(ivFileObj.read())
    ivFileObj.close()
    print("iv=", iv_data)

    #ct = enc_data.decode('UTF8')
    ct = b64decode(enc_data)
    print("ct=",ct)



except ValueError:
    print("Incorrect decryption")
except KeyError:
    print("Incorrect Key")

keyvalue = b64decode(key)
cipher = AES.new(keyvalue, AES.MODE_CBC, iv_data)
pt = unpad(cipher.decrypt(ct), 16)
print("The message was: ", pt)