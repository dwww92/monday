# 13listtuple.py

# 리스트 list  순서 유지, 중복허용, 변경 가능
# 튜플 tuple   순서 유지, 중복허용, 변경 불가

mylist = ['kim', 78, True, 3.1415, 78, 'kim']
mytuple = ('lee', 54, True, 3.1415, 78, 'lee')

mylist[1]=1200 # 리스트변경가능
mytuple[1]=1200 # 튜플은 변경x # TypeError: 'tuple' object does not support item assignment


print(mylist)
print(mytuple)


print()