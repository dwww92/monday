# 04display.py

import time

# import 문서이름
# 참조할때 game.user_pwd, game.terran()
# from 문서이름 import 전역변수, 함수이름만 

from game import user_id, user_pwd, terran
from game import LG, ruuning
#--------------------------------------------------------------------------------------------------------------------------------------------

# def menuE


#--------------------------------------------------------------------------------------------------------------------------------------------

while flag :
    print()
    num=input('1.등록, 2.출력, 3.수정, 4.삭제, 5.조회, 9.종료>>>')
    if num==9: menuExit()
    elif num==1: menuInsertnew()
    elif num==2: menuAllprint()
    elif num==3: menuEditupdate()
    elif num==4: menuDelete()
    elif num==5: menuFindsearch()
    else : print('처리번호를 잘못 입력 하였습니다.')
    