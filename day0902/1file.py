# 2file.py

# 리턴값 = open(파일,모드w/r/a,인코딩)
# 리턴변수.close
# 임포트 문장 없어요

import time

time.sleep(1)
pathName = 'C:/Mtest/sample.txt'
rfile = open('C:/Mtest','w',encoding='UTF-8')
data= rfile.read()      # 전체
#data= rfile.readline() # 한줄씩처리
print(data)
print('-'*50)
rfile.close()
time.sleep(0.5)
print(pathName,'파일읽기 성공했습니다.')
print()

with open(pathName,'a',encoding='UTF-8') as myfile : 
    while my != '':
        pr



# 생략가능 myfile.close()
time.sleep(0.5)
print(pathName,'sample.txt 파일 저장 성공했습니다. ')
print()