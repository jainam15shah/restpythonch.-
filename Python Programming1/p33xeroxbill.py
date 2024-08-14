print("xerox shope")
print("press b for black & white xerox ")
print("press c for color xerox")
print("press BO for both black & white + color xerox")
op=(input("enter opt =>"))
if op=="b":
    x=int(input("enter the quantity =>"))
    if x<50:
        print("the prize is 5 rupees per page",x*5)
    else:
        print("the prize is 3 rupees per page",x*3)
elif op=="c":
    x=int(input("enter the quantity =>"))
    if x<50:
        print("the prize is 15 rupees per page",x*15)
    else:
        print("the prise is 10 rupees per page",x*10)     
elif op=="BO":
    b1=0
    b2=0
    p1=int(input("enter the quantity =>"))
    if p1<50:
        b1=p1*5
        print("the total prize is",b1)
    else:
        b1=p1*3
        print("the total prize is",b1)
    p2=int(input("enter the quantity =>"))
    if p2<50:
        b2=p2*15
        print("the total prize is",b2)
    else:
        b2=p2*10
        print("the total prize is",b2)



    print("the grand total is",b1+b2)

else:
    print("Wrong opt")