# 06 except.py

x, y = 7, 0


hap, gob, mok, nmg = 0,0,0,0

#처리 연산처리, if제어처리, 반복처리
try : 
    hap = x+y
    mok = x/y # 실행중 연산처리 에러 발생 여깃 문제가 발생 except 로 이동함
    nmg = x%y
    gob = x*y

    print(f'{x}+{y}={hap}')
    print(f'{x}/{y}={mok}')
    print(f'{x}%{y}={nmg}')
    print(f'{x}*{y}={gob}')
except : 
    print('주의 경고!!!! 연산처리 잘못 되었습니다.')


    print()
    print('쇼핑목록')
    print('주차처리')
    print('정산성공')