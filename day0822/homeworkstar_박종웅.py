#hoeworkstar.py

# 100 페이지 while 반복문 사용금지
# 조건 중복 for반복문
# 처리 지역변수, 특정변수 필요없음
# 반복문 대표변수 x,y i,j, a,b
###########################################################################################
# i와 j만 수정 : range의 인수 값은 (1,11,1)로 고정 : 조건문과  pass, break로 조정 
print("------순차-------")
for i in range(1,11,1) :
    if i > 1 :  # 전체반복 1번
        break
    else :
        pass
        for j in range(1,11,1) :
            pass
            print("★"*j)
            if j> 4 : # 한 행에 그려지는 별의 갯수 j+1개
                break
 
print("------역차-------")

for i in range(1,11,1) :
    if i > 1 :  # 전체반복 1번
        break
    else :
        pass
        for j in range(1,11,1) :
            pass
            print("★"*(6-j))

            if j> 5 : # 한 행에 그려지는 별의 갯수 j+1개
                break

################################################################################################

for a in range(1, 6, 1):
     for b in range(a):
        print('★', end='')
     print()
     

print()
   
for a in range(5,0,-1) :
     for b in range(a):
       print('★', end='')
     print()


