# 대칭키를 RSA 공개키 알고리즘을 이용해 암호화하고, key.bin에 저장한다.
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

#key = get_random_bytes(16) #이걸 암호화
pkey = RSA.generate(2048)  #pkey를 이용해서 key를 암호화 && key를 이용해서 txt 파일을 암호화
#print(key)  #b'Q\x94\x95$\x19\x84ja\x01\xabEo\xba\xa6\xb6p'
print(pkey) #Private RSA key at 0x1099BBBE0

private_key = pkey.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = pkey.publickey().export_key()
file_out = open("receiver.pem", "wb")
file_out.write(public_key)
file_out.close()
""""""