# HWjumin_강석민.py
# 2024-08-28 / writer: 별

import datetime

# 문제1) 성별체크 1/3: 남자, 2/4: 여자
# 문제2) 생일
# 문제3) 나이계산 2024 - 년수

def checkJumin(jumin):
    jum1 = jumin.split('-')[0]     # len() 6자릿수 체크
    jum2 = jumin.split('-')[1]    # len() 7자릿수 체크

    if (len(jum1) == 6) and (len(jum2) == 7):
        checkGender(jum2)
        chechBTH(jum1)
        checkAge(jum1)
    else:
        print("주민등록번호를 잘못 입력하셨습니다.")
        

def checkGender(jum2):
# 문제 1)
    if jum2[0] == '1' or jum2[0] == '3' :
        print('남자입니다.')
    elif jum2[0] == '2' or jum2[0] == '4' :
        print('여자입니다.')
    else :
        print('잘못된 주민등록번호입니다.')
        

def chechBTH(jum1) :
# 문제 2)
    print('생일은 {}월 {}일입니다.'.format(jum1[2:4],jum1[4:6]))
    
def checkAge(jum1): 
# 문제 3)
    dt = datetime.datetime.now()
    jyear = int(str(dt)[0:4])
    jbth = int(str(dt)[5:10].replace('-',''))
    bth = int(jum1[2:6])
    age = 0

    if jum1[0] == 0 :
        age = 2000 + int(jum1[0:2])
    else:
        age = 1900 + int(jum1[0:2])

    if bth <= jbth :
        print('나이는 {}살입니다.'.format(jyear - age))
    else :
        print('나이는 {}살입니다.'.format(jyear - age - 1))


def main():
    jumin = '971230-1835064'
    
    if '-' in jumin:
        checkJumin(jumin)  
    else:
        print("주민등록번호를 잘못 입력하셨습니다.")

if __name__ == '__main__':
    main()




print('- ' * 40) 