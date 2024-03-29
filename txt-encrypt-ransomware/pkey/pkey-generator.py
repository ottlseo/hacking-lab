from Crypto.PublicKey import RSA

pkey = RSA.generate(2048)
print(pkey)

private_key = pkey.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = pkey.publickey().export_key()
file_out = open("receiver.pem", "wb")
file_out.write(public_key)
file_out.close()