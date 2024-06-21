#adding all even integers ,odd integers,and float value
a=list(map(eval,input().split()))
e,o,f=0,0,0
for i in range (len(a)):
    if i%2==0:
        e=e+i
    
    elif i%2==1:
        o=o+i
    
print(e,o,f)
        
    
