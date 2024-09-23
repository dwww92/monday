#15list.py

import time

# list :  반복 O, 순서 O
mylist = ['kim', 78, 3.1415, True, 'F', "young", 78]  
print(mylist)
print()
time.sleep(1)

# set : 반복 X, 순서 X
myset={'23', 78, 23,'kim', 78,'kim'}    
print(myset)
time.sleep(1)

# tuple : 수정 X  위도,경도 하지만 리스트로 바꾸어서 수정 가능함
mytuple=('blue', 21, 'A')  
print(mytuple)
time.sleep(1)

# dict : key,value 한쌍으로 이루어짐
mydict={100 : 'naver', 200:'kakao'}   
print(mydict)
print()