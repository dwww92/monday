# 06 comprehension.py

lotto = [34, 7, 19, 42, 6, 21]

for k in range(1,11,1) :
    su = k**2
    print(su, end='\t')

print()

for k in range(1,11,1) : 
    su = pow(k,2)
    print(su, end='\t')

message = ['spam','ham','spam','ham','spam','spam']



print()
#문제 1 for 반복 ~ if
mylist = [ a**2 for k in range(1,11,1)]
print(mylist)
print()

for k in message : 
    if k=='spam' :
        print(k,end='')
        message_cnt = message_cnt + 1



#문제 2 comprehension 처리
방법1 temp_list = [ k for k in message if k=='spam']


# 문제 3 
# spam =0, ham =1, dummy=[0,1,0,1,] ret = []
# message = ['spam','ham','spam','ham','spam','spam']
myset = { c**2 for k in range(1,11,1)}
print(myset)
print()