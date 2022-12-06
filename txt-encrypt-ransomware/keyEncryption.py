# 대칭키를 RSA 공개키 알고리즘을 이용해 암호화하고, key.bin에 저장한다.
from Crypto.PublicKey import RSA

#key = b'ZRoX8irxKFjGgVw8cY4MGA=='
key = RSA.generate(2048)
print(key) #Private RSA key at 0x1099BBBE0
"""
private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()
file_out = open("key.bin", "wb")
file_out.write(public_key)
file_out.close()
"""