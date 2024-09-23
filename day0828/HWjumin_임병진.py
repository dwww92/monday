# HWjumin.py
# 2024. 08. 28 (writer: B. Lim)

import time

def checkLen(f, r):
    return True if len(f) == 6 and len(r) ==7 else False

def printError():
    return "Wrong Input. Try Again."

def checkGen(r):
    if r[0] == "1" or r[0] == "3":
        G= "M"
    elif r[0] == "2" or r[0] == "4":
        G= "F"
    else:
        G = printError()
    return G

def getDay():
    localtime = time.localtime() 
    cur_year = localtime.tm_year
    cur_month = localtime.tm_mon
    cur_day = localtime.tm_mday
    return cur_year, cur_month, cur_day

def checkBday(f):
    return f[2:4]+'.'+f[4:]

def isBday(bday, cur_month, cur_day):
    b_month = bday.split('.')[0]
    b_day = bday.split('.')[1]
    return "HBD" if cur_month == int(b_month) and cur_day == int(b_day) else "Not a B-day"

def checkAge(f, r, year):
    if r[0] == '1' or r[0] == '2':
        born_year = '19'+ f[:2]
    elif r[0] == '3' or r[0] == '4':
        born_year = '20'+f[:2]
    else:
        born_year = year
    return int(born_year)

def insert_pid():
    flag = False
    while not flag:
        pid = input("Input your PID with '-': ")
        f = pid.split('-')[0]
        r = pid.split('-')[1]
        if checkLen(f,r):
            flag = True
        else:
            print(printError())
    return f, r

def pid_service(f, r):
    num = -1
    while num != 9:
        print("1. Gender | 2. Bday | 3. Age | 9. Quit")
        num = int(input("Choose your Service : "))
        if num == 1:
            print(checkGen(r))
        elif num == 2:
            _, cur_m, cur_d = getDay()
            birthday = checkBday(f)
            print(birthday)
            print(isBday(birthday, cur_m, cur_d))
        elif num == 3:
            cur_y, _, _ = getDay()
            print(cur_y - checkAge(f,r,cur_y))
        elif num == 9:
            break
        else:
            print(printError())

def pid_program():
    pid_front, pid_rear = insert_pid()
    pid_service(pid_front, pid_rear)
    print("THX")

pid_program()
