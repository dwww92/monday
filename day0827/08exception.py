# 08 exception.py

import time

# dan =3
# for k in range (1,10,1) :
#     print(f'{dan}*{k}={dan*k}')
#     time.sleep(0.5)


# print()
# time.sleep()
# print('포인트 7점 획득')
# print('포인트 5점 이상이면 vip자격 만족대상입니다.')

# print()
# print('- '*50)


#문제1 dan입력 키보드 input(), 형변환
#문제2 dan입력 범위 정수 1이상 2~9사이 숫자만 입력
#문제3 예외처리 try: ~ except: ~

#처리 연산처리, if제어처리, 반복처리

x,y =0,0
hap,gob,mok,nmg = 0, 0, 0, 0

x = int(input('x정수입력(0숫자제외)>>>'))
y = int(input('y정수입력(0숫자제외)>>>'))

try : 
    hap = x+y
    mok = x/y # 실행중 연산처리 에러 발생 여깃 문제가 발생 except 로 이동함
    nmg = x%y
    gob = x*y

    print(f'{x}+{y}={hap}')
    print(f'{x}/{y}={mok}')
    print(f'{x}%{y}={nmg}')
    print(f'{x}*{y}={gob}')
except Exception as ex: 
    print('에러발생이유', ex)
    print('주의 경고!!!! 연산처리 잘못 되었습니다.')


print()
print('쇼핑목록')
print('주차처리')
print('정산성공')