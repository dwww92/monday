# 05ospath.py

# 리턴값 = open(파일,모드w/r/a,인코딩)
# 리턴변수.close
# 임포트 문장 없어요

import sys
import os.path


file = 'C:/Mtest/kakao.txt'
save_path = os.path.abspath('C:/Mtest/kakao.txt')
try : 
    pass

    if not os.path.exists(save_path) : 
        pass # 파일이 없다면 경고 파일저장, 읽기
        print(save_path,'대상 파일이 존재하지 않습니다.')
        sys.exit()
    else : 
        pass 

    with open(file,'r',encoding='UTF-8') as myfile : 
        for data in myfile.readlines():
            print(data,end='')

except Exception as EX : 
    print('에러 이유 확인', EX)


