def max2(n,n2):
    if n<n2:
        print("n2 is max")
    else:
        print("n is max")
def add(n,n2):
    print("add ", n+n2)
def cube(n):
    print("cube ",n**3)

n=int(input("enter the number "))
n2=int(input("enter the number "))   
add(n,n2)
max2(n,n2)
cube(n)