# 03testcal.py


# 변수선언 및 초기화
a = 7
b = 2

hap,sub,gob,mok,nmg =0,0,0,0,0

# x,y,z =0,0,0

x,y,z =False,False,False # 0초기화보다는 False 권장함 BOOL 타입

hap=a+b
print(a+b)
print(hap)

x=a>b
print(a>b)
print(x)

# 관계연산 <, >, <=, >=, ==, !=
# 논리연산 and or not is in

x = (a> b)
y = (a==b)
z = (a!=b)


x = ((a>=b) and (b>=c))
y = ((a==b) or (b>=c))
z = (a!=b)

print('논리연산 and or test')
print(x) # True
print(y) # False
print(z) # True

# a,b = 7,2


# 컴퓨터 언어 language 연산에서 산술, 관계, 논리 and or not
print()