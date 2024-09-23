# 09 resub.py

import re

phone ='010-7800-1234 박이썬'


#힌트 re.sub('1패턴', '2변경작용', phone)
model = re.sub('-[0-9]{4}-', '-****-', phone)

print(phone)
print(model)




# msg = 'my best is blue myjava my cherry blue my python'
# x = re.findall('my',msg)
# y = re.findall('blue',msg) 
# z = re.findall('red',msg)

# print(x)
# print(y) # 두번 들었다면 ['blue', 'blue'] 출력
# print(z) # 없다면 에러대신 []출력
# print()



# # 원래 내용을 재할당한다. 
# msg = 'my best %#@& 245 오렌지 수박 cherry as tea'

# result1 = re.findall('[\w]',msg)
# result2 = re.findall('[\W]',msg) # 비권장
# result3 = re.findall('[a-zA-Z0-9가-힣]+',msg)
# result4 = re.findall('[^a-zA-Z0-9가-힣]+',msg)

# print(result1)
# print(result2)
# print(result3)
# print(result4)

# info1 = re.findall('[a-zA-Z0-9]{3,7}',msg)
# info1 = re.findall('[숫자와문자]{시작자리수,끝자리수}',msg)
# info2 = re.findall('[a-zA-Z0-9]{3,7}',msg)

# print(info1)
# print(info2)



my = re.findall('[a-zA-Z]{7,10}',msg)

if my :
    print(my)
else :
    print('[a-zA-Z]{7,10} 조건에 맞는 데이터 없습니다.')


