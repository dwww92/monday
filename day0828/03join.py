# 03join.py


url = 'www.google.com'
print(url)

myret = url.split('.')


ct = ';' # '공백'  join이면 효과 1배 확대
print(ct.join(url)) # w;w;w;.;g;o;o;g;l;e;.;c;o;m