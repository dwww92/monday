# 11gugudan.py 문서 함수

# 파이썬 함수 def 함수이름() : 
# 파이썬 함수 매개인자
# 파이썬 함수 리턴값

# 내장함수
# list(), len(), tuple(), set()
# int(), round(), print(), input()

import time

# 리턴값X, 매개인자X 일반함수
def gugudan(dan) : 
    for k in range(1,10,1) : 
        print(f'{dan}*{k}={k*dan}')
        time.sleep(0.3)

mydata = 0

try : 
    mydata = int(input('단입력>>>'))
except :
    print('정수 숫자를 입력하세요(1~9 사이를 숫자입력하세요)')