import string
import collections
from binascii import unhexlify, hexlify

mostPopular = "etaoin shrdlu"


def xorWithByte(a, byte):
    ret = [ chr(i^byte) for i in a]
    return "".join(ret)

a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
a = unhexlify(a)

for i in range(0xff):
    result = xorWithByte(a, i)

    stringOk = True

    # Filter only printable strings
    for c in result:
        if not c in string.printable:
            stringOk = False
            break


    # Filter string with matching characters
    normalized = result.lower()
    charStats = collections.Counter(normalized)
    frequent = charStats.most_common(3)
    for c, _ in frequent:
        if not c in mostPopular:
            stringOk = False


    if stringOk:
        print(result)



