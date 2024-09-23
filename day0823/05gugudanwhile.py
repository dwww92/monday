#05gugudanfor.py

import time


# 
# dan = int(input('원하는 단입력>>>'))
# for k in range(1,10,1) :
#     #print(dan,'*',k,'=',(dan*k))
#     print(f'{dan}*{k}={dan*k}')     # f를 넣어 펑션으로 작동하게 한다. 넣지 않으면 액면 그대로 출력 되기 때문에 
#     time.sleep(1)                   # 1초 만 대기 : 크롤링 할때 단계적으로 시간을 주기도 함 

data = int(input('원하는 단입력>>>'))
dan = int(data)

k=0

while True : 
    print(f'{dan}*{k}={dan*k}')     # f를 넣어 펑션으로 작동하게 한다. 넣지 않으면 액면 그대로 출력 되기 때문에 
    k = k+1
    time.sleep(0.5)                 # 1초 만 대기 : 크롤링 할때 단계적으로 시간을 주기도 함 
    if k == 10 : 
        break