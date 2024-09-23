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

# 첫번째 a, hap 1~5출력 누적
'''
1 1
2 3
3 6
4 10
5 15
'''

a = a+1; hap=hap+a; print(a,hap)
a = a+1; hap=hap+a; print(a,hap)
a = a+1; hap=hap+a; print(a,hap)
a = a+1; hap=hap+a; print(a,hap)
a = a+1; hap=hap+a; print(a,hap)

print("------------")

# 변수 재사용할때 초기화 점심식사후
# for 반복문, 대입연산
for k in range(5) :
    
    a = a+1
    hap = hap + a
    print(a,hap)

    print(k,message) 
    # 0부터시작~4 = 5회 처리
    # 10진수


