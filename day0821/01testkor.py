# testscor.ipynb
# 2024-08-21-수요일

#선언부분 = 변수데이터 초기화
#변수 초기화 = 기본값 대입=할당
#변수이름명명은 첫글자 소문자 시작(첫글자 숫자 비권장, 특수문장 비권장)
#변수이름명명은 첫글자 소문자  my_kor, my_sum, my_avg, team_kor
title ='데이터점수'
name = '길동'

kor=90
eng=80
tot=0    #sum  키워드는 내장함수가 있어 쓰지 말것
avg=0.0  #avg  권장

#처리담당 연산(산술,관계,논리), 연산결과 조건if, 반복문(for,while)
tot = (kor+eng)
avg = (kor+eng)/2   # / 몫 처리, % 나머지 값

#처리결과 출력 print('안내문',데이터)
#print() 내장함수는 라인개행포함한다. 빈줄추가 <br>역할
print('이름=', name)
print('국어=', kor)
print('영어=', eng)
print('총점=', tot)

print('평균=', avg)

print("성적처리 종료 수고하셨습니다.")