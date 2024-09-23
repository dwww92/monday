# 17listfor.py

import time

# list :  반복 O, 순서 O
mylist = ['tea', 7]  
print(mylist)

mylist.append('파이썬')
print(mylist)

mylist.append(23)
print(mylist)

mylist.insert(1,'blue')
print(mylist)
print('-'*50)
#최종결과 ['kakao', 'blue', 94, '파이썬', 23]

# 수정할때 
mylist[0] = 'kakao'
mylist[2] = 94
print(mylist)

#삭제 del, remove, pop
mylist.pop(1)
print(mylist)

mylist.sort()
# 주의사항 sort()적용은 같은 타입만 가능
# for a in mylist :
# print(a,end='')

for a in mylist : 
    print(a)

# for 반복문 출력
# for 반복문 연습 1 2 3 4 5 6 7 8 9 10

su=0
for k in range(10) :
    su = su + 1 
    print(su, end=' ')
