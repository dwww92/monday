# 02split.py


url = 'www.google.com'
print(url)

myret = url.split('.')
print(myret)
print(url.split('.'))
print(list(url)) # 최소단위로 쪼갠다 심지어 공백까지 들어 간다. 비권장


print()