n=int(input("enter limit="))
s=1
for i in range(n,0,-1):
    print(i,end=" * ")
    s=s*i

print("fact=",s)    
