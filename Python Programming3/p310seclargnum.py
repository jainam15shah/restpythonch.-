import random
n=int(input("enter the limit"))
l1=[]
for i in range(1,n+1):
    y=random.randint(0,300)
    l1.append(y)
    m=l1[0]
    for x in l1:
        if m<x:
            m=x
t=m
m=0
for x in l1:
    if t==x:
        pass
    elif m<x:
        m=x

print(l1)
print("second larg. num.= ",m)
