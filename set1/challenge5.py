import string
from binascii import unhexlify, hexlify

def xorStrings(a, b):
    if len(b) > len(a):
        a,b = b,a
    # Assume len(a) > len(b)

    ret = [ chr(ord(c)^ord(b[i % len(b)])) for i,c in enumerate(a) ]
    return "".join(ret)

s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
k = "ICE"
print(hexlify(xorStrings(s,k).encode()).decode())
