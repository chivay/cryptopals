import base64
from binascii import unhexlify


hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
hexString = unhexlify(hexString)

based64 = base64.b64encode(hexString)

print(based64.decode())
