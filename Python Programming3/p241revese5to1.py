n=5
x=1
for i in range(1,n):
    for j in range(n-1,i-1,-1):
        print(x,end=" ")
        x=x+1    
    print("")