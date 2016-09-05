
def splitIntoChunks(lst, size):
    n = len(lst)
    return [ lst[i:i+size]  for i in range(0,n, size) ]


blockSize = 16 # bytes
chunkSize = blockSize * 2 # 2 chars per byte
ciphertexts = []

with open("8.txt") as f:
    while True:
        l = f.readline()
        if not l:
            break

        ciphertexts.append(l.strip())



for c in ciphertexts:
    chunks = splitIntoChunks(c, chunkSize)

    stat = {}

    for chk in chunks:
        if not chk in stat.keys():
            stat[chk] = 1
        else:
            stat[chk] += 1
    # If every block appears only once
    if len(c) == len(stat.keys()) * chunkSize:
        continue

    for chk in chunks:
        print(chk)


