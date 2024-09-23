# 16defreturn.py

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

