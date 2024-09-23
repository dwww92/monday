# 05 lotto.py

lotto = [34, 7, 19, 42, 6, 21]

# for k in range(1,11,1) :
#     su = k**2
#     print(su, end='\t')

# print()

# for k in range(1,11,1) : 
#     su = pow(k,2)
#     print(su, end='\t')

# print()

mylist = [ k**2 for k in range(1,11,1)]
print(mylist)
print()

mytuple = ( pow(k,2) for k in range(1,11,1))
print(mytuple)
print()

myset = { k**2 for k in range(1,11,1)}
print(myset)
print()