n=int(input("enter the limit "))
for i in range(1,30):
    y=0
    n=i
    for i in range(2,n//2):
        if n%i==0:
            y=1
            break
    if y==0: 
        print(n,"is prime number ")
    else:
        print(n,"is not a prime number ")
