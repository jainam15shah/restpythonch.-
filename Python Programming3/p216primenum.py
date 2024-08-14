n=int(input("enter the number "))
y=0
for i in range(2,n//2):
    if n%i==0:
        y=1
        break
if y==0: 
    print(n,"is prime number ")
else:
    print(n,"is not a prime number ")