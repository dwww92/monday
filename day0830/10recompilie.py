# 10 recompilie.py

import re

phone ='010-7800-1234 박이썬'

data = '''
kim 840916-1094852
lee 921207-2059326
tea 981024-1674938
'''

# compile('\d{6}-\d{7}')적용 후 sub()확인
# 문자열 함수 for~~if~~data[시작위치]
# 정규식 re.sub('-[0-9]{4}-','-****-',phone)

# 정규식 compile(), sub(1,2,3), 다른방법
# kim 840916-******* 

pattern = re.compile('(\d{6})[-](\d{7})')
first = pattern.sub('<1>-*******',data)

print(first) # 비권장
print(data)

two =re.sub('[0-9]{7}','*******',data)#  권장
print(two)