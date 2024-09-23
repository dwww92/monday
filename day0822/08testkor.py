# 08testkor.py

# 문자열, list, tuple, set, dict
# 반복데이터 사용

'''
for 변수대표k in range(5) :  
    5회 처리 0~4까지 5회 처리
    
for 변수대표k in range(1,5) :  
    4회 처리 0~4까지 4회 처리
    
for 변수대표k in range(1,10,1) :  
    4회 처리 0~4까지 4회 처리
    1씩 증가일때 3번째 1생략

while 조건 : 
    조건 만족시 루프 loop처리
    무한루프처리일때 if 제어문으로 break 반복 탈출
'''

# for, while 연습할때 사용 a,b,hap,tot

a,b=0,0
hap,tot=0,0

message = 'hello 길동!!!'
print(message)
print(message)
print(message)
print(message)
print(message)
print(message)
print()

for k in range(5) :
    print(k,message) 
    # 0부터시작~4 = 5회 처리
    # 10진수


