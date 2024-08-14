n=int(input("enter the limit= "))
s1=0
c1=0
s2=0
c2=0
for i in range(1,n+1):
    if i%2==0:
        s1=s1+i
        c1=c1+1
        print(i,"is even number")
    else:
        s2=s2+i
        c2=c2+1
        print(i,"is odd number")


print("the count of even no is=",c1)
print("the sum of even no is=",s1)
print("the count of odd no is=",c2)
print("the sum of odd no is=",s2)


