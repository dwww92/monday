# 08jumin.py

import datetime
import time


jumin = '971230-1835064'

# 문제1 성별체크 1/3 남자 2/4여자
# 문제2 생일 12월 30일
# 문제3 나이계산 2024-1997

# 주민번호 앞자리 추출
myret = jumin.split('-')
gender = (myret)[1][0:1]



# 문제1 성별체크 1/3 남자 2/4여자
if gender =='1' or gender =='3' :
    print('남자입니다.')
else :
    print('여자입니다.')



# 문제2 생일 12월 30일
y = datetime.datetime.now()
    # print(y)
z = str(y) # 문자열 처리
    # print(z)
birday = z[0:10]

if birday == '2024-12-30' :
    print('생일축하합니다.')
else : 
    print('오늘은 생일이 아닙니다.', '오늘 : ', birday )



# 문제3 나이계산 2024-1997

myarea = 0 # 태어난 년도

if gender =='1' or '2' : 
   myarea = 1900+int((myret)[0][0:2])
else :
   myarea = 2000+int((myret)[0][0:2])  

myage = int(z[0:4]) - myarea

print('나이는 ',myage,'살 입니다.')

