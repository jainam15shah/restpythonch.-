n=5
x=1
for i in range(1,n+1):
    x=1
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(1,n+1):
        print(x,end=" ")
        x=x+1        
    print("")