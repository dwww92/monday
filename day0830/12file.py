# 12file.py

# 리턴값 = open(파일,모드w/r/a,인코딩)
# 리턴변수.close
# 임포트 문장 없어요

import time

time.sleep(1)
pathName = 'C:/Mtest/sample.txt'
wfile = open('C:/Mtest','w',encoding='UTF-8')
name = input('이름입력>>>')
age = input('나이입력>>>')
juso = input('주소입력>>>')

with open(pathName,'a',encoding='UTF-8') as myfile : 
    pass

    wfile.write(name)
    wfile.write(age)
    wfile.write(juso)
    wfile.close() #추천권장

time.sleep(0.5)
print(pathName,'sample.txt 파일 저장 성공했습니다. ')
print()