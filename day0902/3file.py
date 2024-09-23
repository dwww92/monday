# 2file.py

# 리턴값 = open(파일,모드w/r/a,인코딩)
# 리턴변수.close
# 임포트 문장 없어요

import time

time.sleep(1)
fileName = 'C:/Mtest/kakao.txt'


with open(fileName,'r',encoding='UTF-8') as myfile : 
    while my != '':
        print(my)



# 생략가능 myfile.close()
time.sleep(0.5)
print(pathName,'sample.txt 파일 저장 성공했습니다. ')
print()