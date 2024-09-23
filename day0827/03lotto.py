#03lotto.py

lotto = [23,19,5,42,36,27,5,42]
myset = set(lotto) # 중복데이터를 관리한다. 응모할때 하나 데이터유지 filtering 
print(myset)
lotto = list(myset)
lotto.sort() # 오름차순 a,b,c ~~~~ 1,2,3~~~~~



print(lotto)
print()


mylength = len(lotto)

if mylength < 6 : 
    print('항목 하나 추가하셔야 처리 가능')
elif mylength > 6 :
    
    print('항목 데이터 초과입니다\n 다시 확인하세요')
elif mylength == 6 : 
    print('데이터항목 정상입니다.')

# 문제 lotto갯수 6개 아니면 추가 
# len()전역함수

# for k in lotto

# 조건 1 : 숫자 6개
# 조건 2 : 중복숫자 제거
# 조건 3 : 정수숫자로만 구성 문자x, 실수x
