# 06 re.py

import re


msg = 'my best% Flu_it is blue%#357cherry'

info1 = re.findall('[a-zA-Z0-9]{3,7}',msg)
info2 = re.findall('[a-zA-Z0-9]{3,7}',msg)

print(info1)
print(info2)



my = re.findall('[a-zA-Z]{7,10}',msg)

if my :
    print(my)
else :
    print('[a-zA-Z]{7,10} 조건에 맞는 데이터 없습니다.')