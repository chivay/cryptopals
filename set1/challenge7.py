import base64
from Crypto.Cipher import AES


unpad = lambda s: s[0:-s[-1]]

b64 = ""
with open("7.txt") as f:
    while True:
        l = f.readline()
        b64 += l.strip()

        if not l:
            break

ciphertext = base64.b64decode(b64)
key = "YELLOW SUBMARINE"

cipher = AES.AESCipher(key, AES.MODE_ECB)

print(unpad(cipher.decrypt(ciphertext)).decode())
