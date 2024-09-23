# 07 exceptinput.py

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

try : 
    dan = int(input('단수를 입력하세요 >>'))
    if dan < 2 and dan > 9 :
        pass
        print('숫자범위는 2~9 사이 숫자입니다. \n 다시 입력하세요')
        for k in range (1,10,1) :
            print(f'{dan}*{k}={dan*k}')
            time.sleep(0.5)
except :
    print('잘못된 데이터 입니다. ')