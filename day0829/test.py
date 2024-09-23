# test.py

# day0829
# 문제1 변수사용, 키보드입력, 나이는 숫자
# 문제2 나이 입력 범위를 20~70 사이





# name = input('이름 입력>>>')
# age = int(input('나이 입력>>>'))
# gender = input('남자입니까?>>>')
def getPeer(age):
    #세대
    peer = 'unknown'
    if age < 20 :
        peer = '청소년'
    elif 20 < age < 31 :
        peer = '청년'
    elif 31 < age < 66 :
        peer = '중년'
    elif 66 < age  :
        peer = '노년'
    else : 
        print("올바르지 않은 나이입니다..-main")
    return peer


#남자인지 아닌지
def getGender(gender):
    areUman = ''
    if gender == '남자' or gender == '남' or gender == 'man' or gender == '예' :
        areUman = True
    elif gender == '여자' or gender == '여' or gender == 'woman' or gender == '아니오'  :
        areUman = False
    else : 
        print('적절하지 않은 답변입니다.')
    return areUman




def printInfo(name, age, gender):
    try:
        print(name)
        print(age)
        print(gender)
        name1 = name
        gen1 = getGender(gender)
        age1 = getPeer(age)
        print(name1)
        print(gen1)
        print(age1)
        info = "당신은 {}살 {}이고, 생일은 {}입니다.".format(name1, gen1, age1)
        print(info)
    except:
        print("올바르지 않은 정보 입력입니다.")


def main():
    name = input('이름 입력>>>')
    age = int(input('나이 입력>>>'))
    gender = input('남자입니까?>>>')
    printInfo()


while True:
    main()
