# 06 testpickle.py

# open(1파일명, 모드wb/rb, 인코딩)
# dump 쓰기 / load 읽기
# 피클로 파일처리 import


import pickle



fileName = 'kakao.txt'
mybest = {'슈퍼맨superman': 9.72, '아이ironman' : 7.45 }
file = open(fileName,'wb')
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


