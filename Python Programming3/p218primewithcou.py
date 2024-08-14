st=int(input("enter the starting "))
en=int(input("enter the ending "))
c=0
for i in range(st,en+1):
    y=0
    n=i
    for i in range(2,n//2):
        if n%i==0:
            y=1
            break
    if y==0: 
        print(n,"is prime number ")
        c+=1

print("total prime numbers " ,c) 