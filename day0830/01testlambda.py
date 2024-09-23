
# 람다식은 import 기술안함, 키워드 lamda 기술

# 01
def mycal(su) : 
    pass
    cal = 3*su+8
    # return cal 굳이 변수 주지 않고 밑처럼 식을 주기도 한다. 
    return 3*su+8

print('일반식', mycal(5))
#print('람다식',(lambda 매개인자: 수식)(매개인자 자리에 넣을 인자값))
print('람다식',(lambda su: 3*su+8)(5))
my1 = lambda su: 3*su+8 # 람다는 변수처럼 쓸 수도 있다. 

# 02
def myAdd(x,y) : 
    return x+y

print('일반식', myAdd(3,4))
#print('람다식',(lambda 매개인자: 수식)(매개인자 자리에 넣을 인자값))
print('람다식',(lambda x,y: x+y)(3,4))



# 함수엣 계산처리 후 if~else 제어문 리턴값

def myCheck(su) :
    # pass if ~ else 로 짝수인지 홀수인지 체크
    msg = '안내문'

    if su % 2 == 0 : 
        msg = '짝수'
    else :
        msg = '홀수'
    return msg

print('일반식',myCheck(17))
print('람다식',(lambda su : '짝수' if su % 2 == 0 else '홀수' )(17))

myCheck(17)