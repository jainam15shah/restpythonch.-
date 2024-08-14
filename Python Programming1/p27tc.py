print("press 1 for area of circle")
print("press 2 for area of tringle")
op=int(input("enter opt="))
if op==1:
    a=int(input("enter the number="))
    print("area of circle", 3.14*a*a)
elif op==2:
    h=int(input("enter the number="))
    b=int(input("enter the number="))
    print("area of tringle", 1/2*h*b)
else:
        print("wronf opt")