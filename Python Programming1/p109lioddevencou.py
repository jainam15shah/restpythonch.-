import random
n=int(input("enter the limit "))
c=0
l1=[]
for i in range(1,n+1):
    y=random.randint(1,30)
    l1.append(y)
    for x in l1:
        if x%2==0:
            c=c+1
            print(x,"the number is a even")
        else:
            c=c+1
            print(x,"the number is a odd")
        print(x)
print("count",c)