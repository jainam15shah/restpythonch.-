import random
n=int(input("enter the limit "))
l1=[]
for i in range(1,n+1):
    y=random.randint(0,100)
    l1.append(y)
    m=l1[0]
    s=0
    for x in l1:
        s=s+x
        if m<x:
            m=x
print(l1)
print("max= ",m)
print("sum= ",s)