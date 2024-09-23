#hoeworkstar.py

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
