#02test.py

import numbers

mylist = [] # 리스트 선언
mydict = {} # dict 선언


mylist.append('lee')
mylist.append(90)
mylist.append(85)
mylist.append(True)
mylist.insert(1,'빅데이터')

#문제 85 데이터 삭제 : remove(), pop(), del[]
# mylist.remove(85) : 없는 요솔 삭제하려 한다면 에러발생
# mylist.pop(85)    : 
# mylist.del[]

print('- '*50)


for k in mylist : 
    print(k,end='\t')
print()


# 리스트 데이터 갯수   count(), len()
cnt = mylist.count(90)
print('리스트갯수', cnt)
