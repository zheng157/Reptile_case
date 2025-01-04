# 生成一个强密码

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

password = ''

for i in range(8):
    password += random.choice(characters)

print("强密码:", password)