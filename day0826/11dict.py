# 11dict.py

mysite = dict()



mysite['insta'] = 'www.insta.com'
mysite['kakao'] = 'www.kakao.net'
mysite['ibm'] = 'www.ibm.com'
print(mysite)


print(mysite['insta'])
print(mysite['kakao'])
print(mysite['ibm'])
print()

#for 반복문
for i,k in enumerate(mysite) : 
    print(i,':',mysite[k])



for k,v in mysite.items() :
    print(k,':',v)


#dict = k:v 키와 벨류 한쌍으로 이루어짐