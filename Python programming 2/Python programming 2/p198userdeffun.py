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
        
    elif a<b and a<c:
        print("a is less than b and c ")    
    elif b<c and b<a:
        print("b is less than c and a ")            
    else:
        print("c is less than a and b ")    
        
def areaoftringle():
    h=int(input("enter the number"))
    b=int(input("enter the number"))
    print("area of tringle ",1/2*h*b)
def areaofcircle():
    r=int(input("enter the number"))
    print("area of circle ",3.14*r*r)
def table():
    no=int(input("enter the number of table "))
    print(no,"*","1","=",no)
    print(no,"*","2","=",no*2)
    print(no,"*","3","=",no*3)
    print(no,"*","4","=",no*4)
    print(no,"*","5","=",no*5)
    print(no,"*","6","=",no*6)
    print(no,"*","7","=",no*7)
    print(no,"*","8","=",no*8)
    print(no,"*","9","=",no*9)
    print(no,"*","10","=",no*10)
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


cube()
max2()
cube()
max3()
areaoftringle()
areaofcircle()
table()
oddeven()
fact()
squre()