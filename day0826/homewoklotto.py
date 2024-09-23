# homewoklotto.py

import random 

# 로또 1~45사이 숫자
# 로또 정수 
# 반복문 for,while,if

# 난수발생 6개 숫자 중복 체크
# 난수발생후 출력은 sort정렬 
# set이용하지 말것

# 1. list만들기
lotto = []
while len(lotto) != 6:
    lotto.append(random.randint(1,45))
    for k in range(len(lotto)):
        if (lotto.count(lotto[k]>1)) : 
            lotto.pop()
            lotto.append(random.randint(1,45))
        

print(lotto)
lotto.sort()
print(lotto)
