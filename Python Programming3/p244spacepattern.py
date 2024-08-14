n=5
x=n
for i in range(1,n+1):
    x=n
    x=n+1
    x=n+2
    x=n+3
    x=n+4
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(n,i-1,-1):
        print("*",end="")
    
    print("")