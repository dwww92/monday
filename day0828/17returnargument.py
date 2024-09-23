# 17returnargument.py

'''
파이썬에서 함수 정의 시작 키워드 def 함수이름():
사용자정의 함수 매개인자
사용자정의 함수 리턴값 처리후 값을 줄때 리턴 값
사용자정의 함수 매개인자 + 리턴값
'''

def book():
    title = '몽블랑' # 지역변수 = local variable :  휘발성
    return title    

def pay():
    m =7800          # 지역변수 = local variable
    return m

def myCal(x,y,z) : # 메개인자0, 리턴값o
    total = x+y+z
    avg = total//3
    # 3개 데이터를 받아서 계산연산처리 후 최종값 리턴
    return avg

# myCal 함수 호출 90 85 64

data = myCal(90,85,64)
print('myCal함수결과', data)
print('myCal함수결과', myCal(90,85,64))



def gugudan(name,dan): # 메개인자0, 리턴값x
    pass
    # name출력 반복문 dan 출력



#리턴값 X 없는 호출햇 출력하면 엘
def blue():
    color = 'dark'
    #print(데이터 값 출력)

def main():
    print("main 함수")
    data = book()
    value = pay()
    print("책제목", book())
    print("책가격", pay())
    print("블루", blue())

# 함수 단독기술해서 호출
    main()

# 함수호출
# if ___name___ == '___main___ ' : # 생략가능

