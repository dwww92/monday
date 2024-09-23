# HWpickle.py




import pickle
import time
import sys



path = 'C:/Mtest/myCalender.txt'


while True : 
    pass
    num = int(input('1. 스케줄기록 2.스케줄읽기 9.종료>>>'))


    if num==1 : # 피클.dump()
        file = open(path,'wb')
        memo = input("할일입력")
        pickle.dump(memo,file)
        file.close()
        print(path,'저장기록처리 성공했습니다.')
    elif num==2 : # 피클.dump()
        file = open(path,'rb')
        memo = input("할일입력")
        pickle.dump(memo,file)
        file.close()
        print(path,'읽기처리 성공했습니다.')
    elif num==9 : # 피클.dump()
        print('스케줄 피클처리 종료합니다.')
        sys.exit()
    else :
        print('작업번호 오류입니다. ')





