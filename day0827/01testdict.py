#01test.py

import numbers

mylist = [] # 리스트 선언
mydict = {} # dict 선언


mydict[500] = '차박' # mydict[key] = 'value'
mydict[700] = '등산'
mydict[300] = '여행'

for k,v in mydict.items(): 
    print(k,':',v)

print(mydict) #비권장

for k,v in enumerate(mydict) : 
    print((i+1),'',k,mydict[k])




''''''

#28 지목
myJimok = {}

mydict[전] = '전' # mydict[key] = 'value'
mydict[답] = '답'
mydict[과] = '과'
mydict[목] = '목'

mydict[임] = '임'
mydict[광] = '광천지'
mydict[염] = '염전'
mydict[대] = '대'

mydict[장] = '공장'
mydict[학] = '학교용지'
mydict[차] = '주차장'
mydict[주] = '주유소용지'

mydict[창] = '창고용지'
mydict[도] = '도로'
mydict[철] = '철도용지'
mydict[제] = '제방'

mydict[천] = '하천'
mydict[구] = '구거'
mydict[유] = '유지'
mydict[양] = '양어장'

mydict[수] = '수도용지'
mydict[공] = '공원'
mydict[체] = '체육용지'
mydict[원] = '유원지'

mydict[종] = '종교시설'
mydict[사] = '사적지'
mydict[묘] = '묘지'
mydict[잡] = '잡종지'
