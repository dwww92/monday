# 04print.py

# 변수 하나씩 선언, 다중선언
# a=7
# b=4
# ret=0

a,b,ret = 9,4,0
msg=97234


ret=a*b

#print(변수, '문자', ~~), 나열식
print(ret) # 7*4 = 28
print(a,'*',b,'=',ret)
print('{}')

print('{}*{}={}'.format(a,b,ret))

print('{}'.format(msg))        # 정석 97234
print('{:0>10,}'.format(msg))  # 총10자릿수 > 오른쪽맞춤
print('{:0<10,}'.format(msg))  # 총10자릿수 < 왼쪽맞춤
print('{:0^10,}'.format(msg))  # 총10자릿수 ^ 중앙맞춤

print()

print('-'*100)                 # 정석 97234
print('{:0>10,}'.format(msg))
print('{:*>10,}'.format(msg))
print('{:,}'.format(msg))






"""
#print(' {} * {} = {}'.format(a,b,ret))
print('{}*{}={}'.format(a,b,ret))


#print('%d정수 %s문자열 %f실수 %c문자' %(데이터))
print('%d*%d=%d'%(a,b,ret))


#print( f'{변수및값}' )
print('{a}*{b}={ret}')
"""