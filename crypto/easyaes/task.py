#!/usr/bin/python
from Crypto.Cipher import AES
import binascii
from Crypto.Util.number import bytes_to_long
from flag import flag
from key import key

iv = flag.strip(b'd0g3{').strip(b'}')

LENGTH = len(key)
assert LENGTH == 16

hint = os.urandom(4) * 8
print(bytes_to_long(hint)^bytes_to_long(key))

msg = b'Welcome to this competition, I hope you can have fun today!!!!!!'

def encrypto(message):
    aes = AES.new(key,AES.MODE_CBC,iv)
    return aes.encrypt(message)

print(binascii.hexlify(encrypto(msg))[-32:])

'''
56631233292325412205528754798133970783633216936302049893130220461139160682777
b'3c976c92aff4095a23e885b195077b66'
'''
