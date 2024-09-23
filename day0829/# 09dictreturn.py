# 09 dictreturn.py


# 함수의 리턴값 1개이상 처리
# 함수의 매개인자 1개이상 처리 (*args)

def score_procedure() : 
    kor_list = [ score[0] for k in range(1,3,1)]
    eng_list = [ score[1] for k in range(1,3,1)]

    return kor_list

    # return 국어점수합계, 영어점수합계, 국평균, 영평균

score = {
    'kim' : [100,60] ,
    'lee' : [90,77] , 
    'goo' : [82,92]

}

score_procedure(score)

print(kor_list)