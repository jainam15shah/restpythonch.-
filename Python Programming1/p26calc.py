print("press 1 for add")
print("press 2 for sub")
print("press 3 for mul")
print("press 4 for div")
op=int(input("enter opt =>"))
if op==1:
    x=int(input("enter the number =>"))
    y=int(input("enter the number =>"))
    print("add",x+y)
elif op==2:
    x=int(input("enter the number =>"))
    y=int(input("enter the number =>"))
    print("sub",x-y)
elif op==3:
    x=int(input("enter the number =>"))
    y=int(input("enter the number =>"))
    print("mul",x*y)
elif op==4:
    x=int(input("enter the number =>"))
    y=int(input("enter the number =>"))
    print("div",x/y)
else:
    print("wrong opt")

