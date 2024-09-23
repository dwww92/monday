# def.py

# 파이썬 함수 
# def 함수이름(매개) : ~~ return 값

# 함수의 매개인자X, 리턴값
def book() :
    title='몽블랑' # 지역변수 = local variable = 북씨 소유
    return title

def price() :
    pay=7800
    return pay

def main() : 
    print('시작함수 4:32')
    print('main함수 4:33')
    # 에러 print('book함수 title',title)
    value1 = book()
    value2 = price()
    print('book함수 title',value1)
    print('price함수 pay',value2)

main()