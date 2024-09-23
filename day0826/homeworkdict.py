# homwworkdict.py

# 김자바, 이합격, 박패스
# aaa,bbb,ccc, kim, lee, goo


score_dict= {
    '김자바' : [100,60],
    '이합격' : [90,77],
    '강감찬' : [82,34],
    '박현우' : [82,34]
}

list_kor = []
list_eng = []

# for k,v in score_dict.items() :
#     print(k, '' , v)
    


for key in score_dict:
    print(key,sum(score_dict[key]),int(sum(score_dict[key])/len(score_dict[key])))


  #  print(f'{list(score_dict.keys())[k]} {list_kor[k]+list_eng[k]} {(list_kor[k]+list_eng[k])//2}')
    # 아래처럼 출력
   
    # 김자바 160  80  
    # 이합격 167  83  
    # 강감찬 116  58  
    # 박현우 124  62
    