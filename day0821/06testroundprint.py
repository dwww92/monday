# 06testroundprint.py

# 변수 하나씩 선언, 다중선언
# a=9
# b=4
# ret=0

a,b,ret = 9,4,0
mok = 34.56921
print(mok)
print('%d'%(mok))    # 실수지만 정수 34 출력
print('%f'%(mok))    # %f 자릿수 지정안하면 6자릿수까지 출력
print('%6.2f'%(mok)) # %f 자릿수 지정안하면 6자릿수까지 출력
print('%.2f'%(mok)) # %f 자릿수 지정안하면 6자릿수까지 출력

print(round(mok,2)) # 내장함수  round 의 값


ret=a*b


# 내장함수 print(), int(), type(), input('안내문'), str(), sum()
# round(데이터,실수자릿수2)

