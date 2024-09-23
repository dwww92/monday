
for x in range(1,6,1) : 
    pass
    #print(f'{x}*{x}={x*x}')
    print(x,'*',x,'=',(x*x))

for x in range(1,6,1) : 
    print(x,'*',x,'=',str(x*x).rjust(5))
    pass


for x in range(1,6,1) : 
    print(x,'*',x,'=',str(x*x).zfill(5))