# homewoklottoset.py

import random 

# 로또 1~45사이 숫자
# 로또 정수 
# 반복문 for,while,if

# 난수발생 6개 숫자 중복 체크
# 난수발생후 출력은 sort정렬 
# set이용하지 말것

# 2. set만들기
lotto = {}
while len(lotto) != 6:
    lotto.append(random.randint(1,45))
    for k in range(len(lotto)):
        if (lotto.count(lotto[k]>1)) : 
            lotto.pop()
            lotto.append(random.randint(1,45))
        

print(lotto)
lotto.sort()
print(lotto)

'''
나중에 리스트대신 set타입으로 변환
'''
myset = {7, 12, 45, 3, 36, 12}
print(myset)

# my1 = [] 리스트 서로 다른 타입, 같은 데이터 중복O, 순서O
# my2 = () 튜플 변경불가
# my3 = set() 셋 중복 X , 순서 X list(my3)
# my4 = {100:'모니터', 200:'맥북'}
# my5 = dict()함수

#mysite = { } 셋대신 dict타입으로 인식

#mysite = { 1200:'모니터', 2300 : '키보드'} 