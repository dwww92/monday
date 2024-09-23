# 10testfor.py

# 변수선언안하고 for 대표변수 처리

for k in range(1,31,1) : 
    if k%5 == 0:
        print(k,end='\n')  # print() 함수 자동 라인개행포함 엔터기능 <br>
    else :
        print(k,end='\t')  # print() 함수 자동 라인개행포함 탭기능 <br>


print()
print("---------------------------------")
'''
1   2   3   4   5
6   7   8   9   10 
~~~         29  30
'''

