# 11list.py
import time


print("----0.lista----")
time.sleep(0.5)
lista = [2,1,4,5,3]
print(lista)

print("----1.insert----")
time.sleep(0.5)
lista.insert(2,9) # 2번째 위치에 9를 추가한다. 
print(lista)

print("----2.append----")
time.sleep(0.5)
lista.append(7)  # 7을 추가한다.
print(lista)

print("----3.remove----")
time.sleep(0.5)
#lista.remove(8)  # 8을 삭제한다. 없으면 에러 발생
print(lista)

print("----4.pop----")
time.sleep(0.5)
lista.pop(3)     # 3번째 데이터를 삭제한다.
print(lista)

print("----5.reverse----")
time.sleep(0.5)
#lista.sort(reverse=True)     # 3번째 데이터를 삭제한다.
#lista.reverse(lista)     # 3번째 데이터를 삭제한다.
print(lista)





print(lista)
lista.sort()             # 오름차순
lista.sort(reverse=True) # 내림차순
