#09 dictmenu.py

import time
import sys

menu = dict()
flag = True
num,su,sel = 0,0,0
msg,info,message = '안내문', '안내메세지', '안내메세지'


while flag : 
    print()
    num = int(input('1.등록, 2.출력, 3.수정, 4.삭제 , 5.조회, 9.종료>>>'))
    if num == 9 :
        print('딕트처리를 종료합니다.\n')
        # 1. 2개 구문 대신
        # flag = False
        # sys.exit()
        # 2. break 가능
    elif num == 1 : 
        name =input('이름입력 key>>>')
        price =input('가격입력 key>>>')

        menu[name] = price

        print(name,'등록 성공했습니다.')

    elif num == 2 : 
        for i,k in enumerate(menu) : 
            print(i,k,' ',menu[k])
        
    elif num == 3 : 
        name = input('편집대상 키값 입력>>>')
        if menu.get(name) == None:
            print('편집대상 딕트가 key가 없습니다. ')
        else : 
            pass

    elif num == 4 : 
        name = input('삭제대상 키값 입력>>>')
        if menu.get(name) == None:
            print('삭제대상 딕트가 key가 없습니다. ')
        else : 
            #딕트 삭제 
            pass

    elif num == 5 : # 한건만=본인꺼
        name = input('조회검색 key 입력>>>')
        if menu.get(name) == None:
            print('데이터가 없습니다. ')
        else : 
            #딕트 삭제 
            pass
    else: 
        pass

        print('딕트 crud 처리를 종료한다.')
        

# 사용자 정의 함수
# 클래스
# 파일처리 - 파일저장,파일열기
# 예외처리
# crud 
# ㄴcreate(insert=add)
# ㄴread읽기 update수정 delete삭제

mysite = dict() # 100k : 네이버v // 200k : 카카오v
mysite[100] = 'naver'
mysite[200] = 'kakao'
mysite[300] = 'google'

for i,k in enumerate(mysite) : 
    print(i,k,'  ',mysite[k])


for k,v in mysite.items() : 
    print(k,' ',v)

print(mysite[200]) #에러발생
print(mysite.get())


# 출력 items(), enumerate(mysite)
# 수정 100:네이버 100:에이콘