import random
n=int(input("enter the limit "))
l1=[]
for i in range (1,n+1):
    y=random.randint(1,30)
    l1.append(y)
    print(l1)
    for x in l1:
        if x%2==0:
            print(x,"the number is even")
        else:
            print(x,"the number is odd")


