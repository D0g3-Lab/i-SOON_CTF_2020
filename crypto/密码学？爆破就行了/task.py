#!/usr/bin/python2
import hashlib 
from secret import SECRET
from broken_flag import BROKEN_FLAG


flag = 'd0g3{' + hashlib.md5(SECRET).hexdigest() + '}'
broken_flag = 'd0g3{71b2b5616**2a4639**7d979**de964c}'

assert flag[:14] == broken_flag[:14]
assert flag[16:22] == broken_flag[16:22]
assert flag[24:29] == broken_flag[24:29]


ciphier = hashlib.sha256(flag).hexdigest()
print(ciphier)


'''
ciphier = '0596d989a2938e16bcc5d6f89ce709ad9f64d36316ab80408cb6b89b3d7f064a'
'''
