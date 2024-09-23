# 04delpop.py
import time

data = [7,8,9,10,3,5,2,4,1]
data.remove(9) # 9삭제
data.pop() # 2 삭제 맨끝 : 숫자 적지 않으면 맨 뒤요소 삭제
print(data)
del data[2] 
print(data)

time.sleep(1)

del data[1:5] #[시작: 끝+1]
print(data)

time.sleep(0.5)
data = [7,8,9,10,3,5,2,4,1]
# data.clear 정답 빙고 에러 대신 삭제가 되지 않을 뿐
# del data[:] # 전체삭제 비권장
print(data)
print('삭제연습끝 드디어 dict 실습 k:v')

# count (인자가 있어야 함), len(내장함수라 데이터, 집합함수가 들어가야 함, 리스트,딕트,문자열)


# remove, del, pop 제거삭제기능

# remove(데이터값)
# pop(위치)  pop()맨끝
# del 대상[위치]
# clear 전부삭제

# 추가 
# append(), insert(위치,값), add()
# 추가 딕트이름[k300] = dataValue
# 덮어씌어짐 딕트이름[k300] = dataValue