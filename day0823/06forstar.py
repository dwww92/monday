# 06forstar.py

n=6
for i in range(n) :
    for j in range(n-(i+1)) :
        print(' ', end='')      # 공백을 출력함
    for j in range(2*i+1) : 
        print('+', end='')      # '+'를 출력함
    print()


print()