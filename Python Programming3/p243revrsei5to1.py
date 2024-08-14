n=5
x=n
for i in range(1,n+1):
    x=n
    for j in range(n,i-1,-1):
        print(x,end="")
        x=x-1    
    print("")