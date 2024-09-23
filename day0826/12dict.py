# 12dict.py

mysite = dict()



mysite['insta'] = 'www.insta.com'
mysite['kakao'] = 'www.kakao.net'
mysite['ibm'] = 'www.ibm.com'
mysite['naver'] = 'www.naver.com'  # 기존 벨류가 지워지면서 새로 운 벨류가 들어 간다. 

print(mysite)
print()
print(mysite.keys())    # 키값 목록
print()
print(mysite.values())  # 벨류값 목록
print()


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