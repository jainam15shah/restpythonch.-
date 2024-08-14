n=int(input("enter the limit "))
s=0
c=0
for i in range(1,n+1):
    if i%2==0:
        s=s+i
        c=c+1
        print(i)
    
print("count=",c)
print("sum=",s)

