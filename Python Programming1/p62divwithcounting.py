n=int(input("enter the limit "))
d=int(input("enter the divition "))
s=0
c=0
for i in range(1,n+1):
    if i%d==0:
        s=s+i
        c=c+1
        print(i)

print("count=",c)
print("sum=",s)

