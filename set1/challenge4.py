import string
from binascii import unhexlify, hexlify

def xorWithByte(a, byte):
    ret = [ chr(i^byte) for i in a]
    return "".join(ret)

with open("4.txt") as f:

    for line in f.readlines():
        line = unhexlify(line.strip())

        for i in range(0xff):
            result = xorWithByte(line, i)

            stringOk = True


            # Filter only printable strings
            for c in result:
                if not c in string.printable:
                    stringOk = False
                    break
            # Filter string with matching characters
            normalized = result.lower()
            alphabet = string.ascii_letters + " " + "\n"
            for c in normalized:

                if not c in alphabet:
                    stringOk = False

            if stringOk:
                print(result)
