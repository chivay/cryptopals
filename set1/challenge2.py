from binascii import unhexlify, hexlify


def xorStrings(a, b):
    n = min(len(a), len(b))
    ret = [ chr(a[i]^b[i]) for i in range(n)]
    return "".join(ret)


a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"


xored = xorStrings(unhexlify(a),unhexlify(b))

xored = str.encode(xored)

print(hexlify(xored).decode())

