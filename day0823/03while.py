# 03whil.py

# su = 0

# while True :
#     su = su + 1
#     print(su, end='  ')
#     if su == 100 :
#         break

# print()
# print('- '*50)



#문제 1234578910 5를 출력하지 않는다. while문 
su = 0
while True :
    su = su + 1
    if su == 5 :
        continue
    
    print(su, end=' ')
    
    if su == 10 :
        break