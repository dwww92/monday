import os
import pandas as pd
import cx_Oracle  

# pip install oracledb 
#import oracledb     
import time


# 입력된 코드 값
dcode = ''

config = {
    'user' : 'system',
    'password' : '1234',
    'dsn' : '127.0.0.1:1521/xe'  #/xe 우리가 들어가는 서비스 이름
    #'dsn' : 'localhost:1521/xe'
    
}

conn = cx_Oracle.connect(**config)
print('config매개인자타입', type(config))
# conn = cx_Oracle.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe') #이것도 가능
cursor = conn.cursor() # 작업을 위한 커스를 만듬

print("database version: ", conn.version)
print("oracle connect ok success")
print()

# 코드값 중복 체크를 위한 셋
codeset = set()
# 1.기존 코드값을 추출함
def sosiSelectCodeAll():
    msg = 'select * from sosi order by code'
    cursor.execute(msg)
    rows = cursor.fetchall() # fetch 실시간의 데이터 <-> batch 모아서 처리하기 (세금,월급)
    print('rows타입 ', type(rows))
    print()


    for r in rows:
        targetcode = r[0]
        codeset.add(targetcode)


    print(codeset)

# 2.코드 중복 체크
def sosiCodeDupChk():
    # 중복 체크 후 번호 추가
    if dcode not in codeset:
        codeset.add(dcode)
    else : 
        print("이미 중복된 코드 번호 입니다.")

# 3.입력값
def sosiInsert():
    print('\nsosi테이블 신규등록 처리 ')
    dcode = int(input('코드 입력>> '))
    dname = input('이름 입력>> ')
    dtitle = input('제목 입력>> ')
    #dsal = int(input('급여 입력>> '))
    #msg = f"insert into sosi values({dcode},'{dname}','{dtitle}',{dsal}, sysdate, 'D')"      # 실행할 문장을  더블안에 싱글로 넣어 줄 것 

    message = f"select count(*) cnt from sosi where code = {dcode}"

    cursor.execute(message)
    cnt = cursor.fetchone()

    # 코드데이터 입력 후 code 필드값 중복체크/함수탈출/재입력
    # error 이유 unique constraint (SYSTEM.SYS_C007007)
    # 1.신규등록 2.전체출력 3.수정 4.삭제 5.제목조회 9.종료

    # 2.코드 중복 체크
    sosiCodeDupChk()
   

    # 신규 등록하기 전에 select ~~ 
    msg = f"insert into sosi values({dcode},'{dname}','{dtitle}')"      # 실행할 문장을  더블안에 싱글로 넣어 줄 것 
    cursor.execute(msg)
    conn.commit()
    print(dcode , ' 저장 성공했습니다')
    time.sleep(1)



def sosiUpdate() : 

# 1.기존 코드값을 추출함
sosiSelectCodeAll()

# 2.코드 중복 체크
sosiCodeDupChk()

# 3.입력값
sosiInsert()


# sosiSelectAll()
# sosiInsert()
# time.sleep(0.5)
# sosiSelectAll()
# print()