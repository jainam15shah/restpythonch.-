print("press + for add")
print("press - for sub")
print("press * for mul")
print("press / for div")
op=(input("enter opt =>"))
if op=="+":
    x=int(input("enter the number =>"))
    y=int(input("enter the number =>"))
    print("add",x+y)
elif op=="-":
    x=int(input("enter the number =>"))
    y=int(input("enter the number =>"))
    print("sub",x-y)
elif op=="*":
    x=int(input("enter the number =>"))
    y=int(input("enter the number =>"))
    print("mul",x*y)
elif op=="/":
    x=int(input("enter the number =>"))
    y=int(input("enter the number =>"))
    print("div",x/y)
else:
    print("wrong opt")

