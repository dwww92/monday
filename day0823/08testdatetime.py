# 08testdatetime.py


import time
import datetime
# from 파일명클래스 import datetime
# from datetime import datetime


my = time.localtime()
print(my)
print(my.tm_year,'년')
print(my.tm_mon, '월')
print(my.tm_mday,'일')
print(my.tm_wday) # 0 월요일 1 화요일 2 수요일 3 목요일 4 금요일
time.sleep(0.5)
print()

dt = datetime.datetime.now()
print(dt)


print('aaaaaaaaaaaaa')
time.sleep(0.3)
print('bbbbbbbbbbbbb')
time.sleep(0.3)
print('ccccccccccccc')