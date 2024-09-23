#13gugudan

dan = 7
for k in range(1,10,1):
    pass

print()
print('구구단 연습')

'''
파이썬 화면 모니터 출력 print('안내문', 값)
파이썬 키보드 자판 입력 input('안내문')
파이썬 키보드입력데이터 문자로 인식
int("1200") 숫자 1200

'''
print("-----------문자열 그대로 할당한 뒤 합쳤을때 --------------")

a = "120" # or '120'
b = "75"  # or '75'

print(a+b) #12075
# 형변환을 하지 않는다면 문자 취급 되어 그저 이어 붙여져서 출력된다. 
print("-----------int 를 통해 형변환 하였을 때 --------------")

c = int(a) + int(b)

print(int(a) + int(b)) #195
print(c) #195


# 파이썬 내장 함수
# print()
# int()
# round()
# input()

print("-----------구구단 --------------")7

data = input('구구단 입력>>>')
dan = int(data)

for k in range(1,10,1):
    print(dan,'*',k,'=',(dan*k))
