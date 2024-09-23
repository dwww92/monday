# 15defreturn.py

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

def main():
    print("main 함수")
    # 에러 print("책제목", title)
    # 에러 print("책제목", m)
    data = book()
    value = pay()
    print("책제목", data)
    print("책가격", value)
    print("책제목", book())
    print("책가격", pay())
    print("책제목", book) # 번지값 출력 <function book at 0x000001699F188A40>
    print("책가격", pay)  # 번지값 출력  <function pay at 0x000001699F3E9DA0>

if __name__ == '__main__' : 
    main()

# 함수호출
# if ___name___ == '___main___ ' : # 생략가능

