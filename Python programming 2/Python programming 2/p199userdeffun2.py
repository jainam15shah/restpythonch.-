def cube():
    a=int(input("enter the number "))
    print("cube = ",a**3)
def max2():
    a=int(input("enter the number "))
    b=int(input("enter the number "))
    if a>b:
        print("a is greater than b")
    else:
        print("b is greater than a")
def max3():
    a=int(input("enter the number "))
    b=int(input("enter the number "))
    c=int(input("enter the number "))
    if a>b and a>c:
        print("a is greater than b and c ")    
    elif b>c and b>a:
        print("b is greater than c and a ")            
    elif c>a and c>b:
        print("c is greater than a and b ")    
        
def areaoftringle():
    h=int(input("enter the number"))
    b=int(input("enter the number"))
    print("area of tringle ",1/2*h*b)
def areaofcircle():
    r=int(input("enter the number"))
    print("area of tringle ",3.14*r*r)
def table():
    n=int(input("enter the no"))
    i=1
    while i<=10:
        print(n,"*",i,"=",i*n)
        i=i+1
    def oddeven():
        n=int(input("enter the number "))
        if n%2==0:
            print("the number is even")
        else:
            print("the number is odd")
def fact():
    N=int(input("enter the number "))
    i=1
    s=1
    while i<=N:
        print(i,end=" * ")
        s=s*i
        i=i+1

    print("fact ",s)
def squre():
    a=int(input("enter the number "))
    print("squre = ",a**2)


print("Press 1 for cube")
print("Press 2 for square")
print("Press 3 for max2")
print("Press 4 for max3")
print("Press 5 for area of tringle ")
print("Press 6 for area of circle ")
print("Press 7 for table")
print("Press 8 for fact")
print("Press 9 for oddeven")
op=int(input("Emnter opt =>"))
if op==1:
    cube()
if op==2:
    squre()
if op==3:
    max2()
if op==4:
    max3()
if op==5:
    areaoftringle()
if op==6:
    areaofcircle()
if op==7:
    table()
if op==8:
    cube()
if op==9:
    fact()
if op==1:
    oddeven()
max2()
cube()
max3()
areaoftringle()
areaofcircle()
table()
oddeven()
fact()
squre()