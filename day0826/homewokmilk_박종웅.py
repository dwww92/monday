apart = [ 
    [101,102,103,104], 
    [201,202,203,204], 
    [301,302,303,304], 
    [401,402,403,404] 
]

unpaid = [101, 204, 302, 403]

#힌트 중첩 for
'''
for x ~~
    for y ~~
      if 조건 in unpaid 
          우유배달 x
      else :
          우유배달 O
'''

# 101호 우유 배달 중지x
# 102호 우유 배달 계속o
# 103호 우유 배달 계속o
# 104호 우유 배달 계속o

# 201호 우유 배달 계속o
# 202호 우유 배달 계속o
# 203호 우유 배달 계속o
# 204호 우유 배달 중지x

# 301호 우유 배달 계속o
# 302호 우유 배달 중지x
# 303호 우유 배달 계속o
# 304호 우유 배달 계속o

# 401호 우유 배달 계속o
# 402호 우유 배달 계속o
# 403호 우유 배달 중지x
# 404호 우유 배달 계속o

# unpaid = [101, 204, 302, 403]

for x in range(len(apart)) :
    for y in range(len(unpaid)) : 
        allapart = apart[x][y]    # 모든 배달 대상 호수
        unpaidho = unpaid[y]      # 지불하지 않은 호수
        if allapart in unpaid :   # 지불하지 않은 호수에 대상 호수가 포함된다면
            print(allapart,'호 우유 배달 중지x')
        else :
            print(allapart, '호 우유 배달 계속o')
