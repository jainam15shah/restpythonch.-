n=int(input("enter limit="))
s=0
for i in range(1,n+1):
    if i%2==0:
       print(end="")
    else:
       print(i,end=" + ")
       s=s+i

print("sum=",s)      
