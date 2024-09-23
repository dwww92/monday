# 08jumin.py

import datetime
import time


#jumin = '971230-1835064'

# 문제1 성별체크 1/3 남자 2/4여자
# 문제2 생일 12월 30일
# 문제3 나이계산 2024-1997
# 주민번호 앞자리 추출


y = datetime.datetime.now()
z = str(y) # 문자열 처리
birday = z[0:10]


# 문제1 성별체크 1/3 남자 2/4여자 
def getMyGender(gender):
    
    myGen = ''   # M : 남자 / W : 여자 / N : 성별을 알 수 없는 잘못된 값
    if gender =='1' or gender =='3' :
        # print('남자입니다.')
        myGen = '남성'
    elif gender =='2' or gender =='4' : 
        myGen = '여성'   
    else :
        myGen = '성별을 알수 없습니다.'
    return myGen

# 문제2 생일 12월 30일
def getMyBirthday(myret):

    myDay= ''
      
    if birday == (myret)[0][0:4] :
        myDay = '생일 축하 합니다!'
    else : 
        myDay = '생일은 아니지만 좋은 하루 보내세요'
  
    return myDay




# 문제3 나이계산 2024-1997
def getMyAge(gender,myret):

    myAge = 0 # 태어난 년도

    if gender =='1' or '2' : 
        myarea = 1900+int((myret)[0][0:2])
    else :
        myarea = 2000+int((myret)[0][0:2])  

    myAge = int(z[0:4]) - myarea

    return myAge



def main():
    jumin = input("주민등록 번호를 입력해주세요(14 자리 -포함) >> ")
    myret = jumin.split('-')
    gender = (myret)[1][0:1]



    biryear = (myret)[0][0:2]
    birtmonth = (myret)[0][2:4]
    birtdate = (myret)[0][4:6]
    birtday = "{}년 {}월 {}일".format(biryear, birtmonth, birtdate)


    if '-' in jumin :
        myGender = getMyGender(gender) 
        myBirthday = getMyBirthday(myret) 
        myAge = getMyAge(gender,myret)  
        print("성별은 {}이고 나이는 {}세 입니다. 생일은 {}입니다. {} ".format(myGender, myAge, birtday, myBirthday))
    else :
        print("주민등록번호를 잘못 입력하셨습니다.")



if __name__ == '__main__':
    main()

