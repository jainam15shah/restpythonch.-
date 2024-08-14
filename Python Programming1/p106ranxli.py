import random
n=int(input("enter the limit "))
l1=[]
for i in range (1,n+1):
    y=random.randint(1,30)
    l1.append(y)
    for x in l1:
        print(x)

