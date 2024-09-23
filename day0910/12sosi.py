# 12sosi.py

# 오라클 sosi테이블 + 파이썬
import os
import pandas as pd
import cx_Oracle  

# pip install oracledb 
#import oracledb     
import time
       

config = {
    'user' : 'system',
    'password' : '1234',
    'dsn' : '127.0.0.1:1521/xe'  #/xe 우리가 들어가는 서비스 이름
    #'dsn' : 'localhost:1521/xe'
    
}


# conn = oracledb.connect(**config) #오류
# conn = oracledb.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe') #오류
conn = cx_Oracle.connect(**config) # .connect() 라이브러리 상에 존재하는 매서드 # 정석
print('config매개인자타입', type(config))
# conn = cx_Oracle.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe') #이것도 가능
cursor = conn.cursor() # 작업을 위한 커스를 만듬 


print("database version: ", conn.version)
print("oracle connect ok success")
print()


def sosiInsert():
    print('\nsosi테이블 신규등록 처리 ')
    dcode = int(input('코드 입력>> '))
    dname = input('이름 입력>> ')
    dtitle = input('제목 입력>> ')
    dsal = int(input('급여 입력>> '))
    #msg = f"insert into sosi values({dcode},'{dname}','{dtitle}',{dsal}, sysdate, 'D')"      # 실행할 문장을  더블안에 싱글로 넣어 줄 것 

    message = "select"

    # 코드데이터 입력 후 code 필드값 중복체크/함수탈출/재입력
    # error 이유 unique constraint (SYSTEM.SYS_C007007 )
    # 1 신규등록 2 전체출력 3 수정 4 삭제 5.제목조회 9.종료

    # 신규 등록하기 전에 select ~~ 
    msg = f"insert into sosi values({dcode},'{dname}','{dtitle}',{dsal})"      # 실행할 문장을  더블안에 싱글로 넣어 줄 것 
    cursor.execute(msg)
    conn.commit()
    print(dcode , ' 저장 성공했습니다')
    time.sleep(1)



def sosiSelectAll():
    msg = 'select * from sosi order by code'
    cursor.execute(msg)
    rows = cursor.fetchall() # fetch 실시간의 데이터 <-> batch 모아서 처리하기 (세금,월급)
    print('rows타입 ', type(rows))
    print()

    print('%s\t %s\t %10s\t  %4s\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급') )
    for r in rows:
        print(r[0],r[1],r[2],r[3])
        # print('%4d\t %10s\t %10s\t  %4d\t %6s\t %s' %r) 
    print('전체데이터 갯수:' , len(rows))
    print('- ' * 50)
    time.sleep(1)

    #   CODE NAME  TITLE   SAL WDATE    GRADE
    #   ------ ----------- ------ ----- --------
    #   9900 goo   gugu    40 24/09/05   F
    #   8800 aaa   red     46 24/09/05   F


def sosiSelectTitle():
    pass
    print('제목데이터 like조회하세요 ')


def sosiDelete():
    pass
    print('code조회후 삭제처리하세요')


sosiSelectAll()
sosiInsert()
time.sleep(0.5)
sosiSelectAll()
# print()