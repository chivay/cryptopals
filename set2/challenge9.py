
# Do PKCS#7 padding
def pad(s, length):
    overSize = len(s) % length
    toAdd = length - overSize

    if overSize == 0:
        return s
    padding = bytes([toAdd] * toAdd)

    return b''.join([s, padding])

print(pad(b'YELLOW SUBMARINE', 20))

