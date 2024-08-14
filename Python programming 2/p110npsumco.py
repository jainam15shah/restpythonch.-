import random
n=int(input("enter the limit "))
c1=0
c2=0
s1=0
s2=0
l1=[]
for i in range(1,n+1):
    y=random.randint(-20,30)
    l1.append(y)
    for x in l1:
        if x>0:

            c1=c1+1
            s1=s1+i
            print(x,"the number is a pos")
        else:
            c2=c2+1
            s2=s2+i
            print(x,"the number is a neg")
        print(x)
print("count",c1)
print("count",c2)
print("sum",s1)
print("sum",s2)