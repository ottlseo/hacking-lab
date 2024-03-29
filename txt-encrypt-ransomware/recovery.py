#-*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os, sys, glob

## 1) Key Recovery (RSA decryption)
key_file_in = open("key.bin", "rb")
private_key = RSA.import_key(open("pkey/private.pem").read())
enc_key = key_file_in.read(private_key.size_in_bytes())
cipher_rsa = PKCS1_OAEP.new(private_key)
key = cipher_rsa.decrypt(enc_key)
key_file_in.close()

key_file_out = open("key.txt", 'w', encoding='UTF8')
key_file_out.write(b64encode(key).decode('UTF8'))
key_file_out.close()

## 2) File Recovery (AES decryption)
for file in glob.glob("*.enc"):
    filename = str(file).split('.')[0]
    encFileObj = open(file, 'rb')
    enc_data = encFileObj.read()
    encFileObj.close()
    ct = b64decode(enc_data)

    ivFileObj = open("iv/" + filename + "_iv.txt", "rb")
    iv = b64decode(ivFileObj.read())
    ivFileObj.close()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    # print("The message was: ", pt)

    plain_file_name = str(filename) + ".txt"
    plainFileObj = open(plain_file_name, 'w', encoding='UTF8')
    plainFileObj.write(pt.decode('utf-8'))
    plainFileObj.close()
    """
    try:
        filename = str(file).split('.')[0]
        encFileObj = open(file, 'rb')
        enc_data = encFileObj.read()
        encFileObj.close()
        ct = b64decode(enc_data)

        ivFileObj = open("iv/"+filename+"_iv.txt", "rb")
        iv = b64decode(ivFileObj.read())
        ivFileObj.close()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), 16)
        #print("The message was: ", pt)

        plain_file_name = str(filename)+".txt"
        plainFileObj = open(plain_file_name, 'w', encoding='UTF8')
        plainFileObj.write(pt.decode('utf-8'))
        plainFileObj.close()

    except ValueError:
        print("Incorrect decryption")
    except KeyError:
        print("Incorrect Key")

"""