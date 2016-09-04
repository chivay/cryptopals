import base64
from itertools import cycle

freq = {
'A': 8.167,
'B': 1.492,
'C': 2.782,
'D': 4.253,
'E': 12.702,
' ': 12.702, # Space is ~ as common as E
'F': 2.228,
'G': 2.015,
'H': 6.094,
'I': 6.966,
'J': 0.153,
'K': 0.772,
'L': 4.025,
'M': 2.406,
'N': 6.749,
'O': 7.507,
'P': 1.929,
'Q': 0.095,
'R': 5.987,
'S': 6.327,
'T': 9.056,
'U': 2.758,
'V': 0.978,
'W': 2.360,
'X': 0.150,
'Y': 1.974,
'Z': 0.074,
}


def xorArrays(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    return [ a^b for a,b in zip(s1, cycle(s2))]

def splitIntoChunks(lst, size):
    n = len(lst)
    return [ lst[i:i+size]  for i in range(0,n, size) ]


def countBits(x):
    cnt = 0
    while x != 0:
        cnt += (x & 0x1)
        x >>= 1
    return cnt

def hammingDistance(s1, s2):
    total = 0
    for b,c in zip(s1, s2):
        total += countBits(b^c)
    return total


a = "this is a test".encode()
b = "wokka wokka!!!".encode()

# Check if distance function is working
assert hammingDistance(a,b) == 37

b64 = ""
with open("6.txt") as f:
    while True:
        l = f.readline()
        b64 += l.strip()

        if not l:
            break

c = base64.b64decode(b64)

maxLen = 40

distances = []

# Find most probable keysize
for keysize in range(2, maxLen + 1):
    chunks = splitIntoChunks(c, keysize)

    first = chunks[0]

    localDistances = []
    for chunk in chunks[1:]:
        distance = hammingDistance(first, chunk)
        distance = distance / keysize
        localDistances.append(distance)

    distances.append( (keysize, sum(localDistances)/len(localDistances)) )
    print("[*] Keysize: {:2}, distance: {:.2f}".format(keysize, distance))

distances = sorted(distances, key=lambda t: t[1])

# Get only top 1 match
keyLengths = [ t[0] for t in distances[0:1]]
print("[*] Possible key lengths: {}".format(keyLengths))


for length in keyLengths:
    print("[*] Trying keysize: {}".format(length))
    chunks = splitIntoChunks(c, length)

    # Add padding for last chunk
    paddedBytes = length - len(chunks[-1])
    chunks[-1] = chunks[-1].ljust(length, b'\0')

    key = []

    # Iterate over each index and try to crack it
    for idx in range(0, length):
        arr = [ chk[idx]  for chk in chunks]

        bestMatch = 0
        bestScore = -1

        def scoreResult(s):
            score = 0
            for byte in s:
                if ord('a') <= byte <= ord('z'):
                    byte -= ord('a') - ord('A')
                ch = chr(byte)
                if ch in freq:
                    score += freq[ch]
            return score

        for x in range(128):
            result = xorArrays(arr, [x])
            score = scoreResult(result)

            #print("Byte: {}, score: {:.0f}".format(x, score))

            if bestScore < score:
                bestScore = score
                bestMatch = x

        key.append(bestMatch)

    deciphered = xorArrays(c, key)
    deciphered = [chr(x) for x in deciphered]
    keyString = ''.join([chr(x) for x in key])
    print("Key: '{}'".format(keyString))
    print("Ciphertext: {}".format("".join(deciphered)))






