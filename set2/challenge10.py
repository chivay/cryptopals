from Crypto.Cipher import AES
from itertools import cycle
import base64

blockSize = 16

def xorBytes(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    return bytes([ a^b for a,b in zip(s1, cycle(s2))])

# Do PKCS#7 padding
def pad(s, length):
    overSize = len(s) % length
    toAdd = length - overSize

    if overSize == 0:
        return s
    padding = bytes([toAdd] * toAdd)

    return b''.join([s, padding])

def encryptBlock(block, key):
    assert len(block) == blockSize

    cipher = AES.AESCipher(key, AES.MODE_ECB)
    return cipher.decrypt(block)

def readFile(filename):
    buf = ''
    with open(filename, 'r') as f:
        while True:
            l = f.readline()
            buf += l.strip()

            if not l:
                break
    return buf

iv = bytes([0] * blockSize)
key = b'YELLOW SUBMARINE'


based = readFile("10.txt")
ciphertext = base64.b64decode(based)


blocks = [ ciphertext[i:i+blockSize] for i in range(0, len(ciphertext), blockSize)]

plaintext = b''

prev = iv
for block in blocks[0: -1]:
    plain = xorBytes(encryptBlock(block, key), prev)
    plaintext += plain
    prev = block


unpad = lambda s: s[0: -s[-1]]

#Decrypt last block and unpad
plain = xorBytes(encryptBlock(blocks[-1], key), prev)
plaintext += unpad(plain)

print(plaintext.decode())
