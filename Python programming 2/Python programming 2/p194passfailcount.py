import random
c1=0
c2=0
d1={}
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    no=i
    mark=random.randint(1,40)
    d1[no]=mark

print("no\tmark")
print("*"*30)
for k,v in d1.items():
    if v>=18:
        print(k,"\t",v,"\tPass")
        c1=c1+1

    else:
        print(k,"\t",v,"\tfail")
        c2=c2+1
print("pass",c1)
print("fail",c2)
print("*"*30)

