# 09tuple.py


t=(30,20, 10,50,63,7,7,67,63,20,30,63)


print('갯수',t.count(10))
# print('갯수',t.count(20))
print('색인',t.index(20))  # 중복되는 숫자의 가장 빠른 순번이 출력된다. 
# print('색인',t.index(40))


print(t)
print()


mylist = list(t)  # 튜플을 그대로 리스트에 담을 수 있다.
print(mylist)
mylist.append(7)
mylist.insert(2,63) # 위치, 값
mylist.remove(20)   # 값
print(mylist)
print()
print(tuple(mylist)) # 수정,삭제,추가 할수 없음



# 에러 :  리스트만 된다. t.append(7)
# 에러 :  리스트만 된다. t.insert(2,76)
# 에러 :  리스트만 된다. t.remove(20)
print()
