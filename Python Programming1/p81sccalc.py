while True:
    print("press + for add")
    print("press - for sub")
    print("press * for mul")
    print("press / for div")
    print("press E for exit")
    op=(input("enter the op "))
    if op=="+":
        x=int(input("enter the no "))
        y=int(input("enter the no "))
        print("add ",x+y)
    elif op=="-":
        x=int(input("enter the no "))
        y=int(input("enter the no "))
        print("sub ",x-y)
    elif op=="*":
        x=int(input("enter the no "))
        y=int(input("enter the no "))
        print("mul ",x*y)
    elif op=="/":
        x=int(input("enter the no "))
        y=int(input("enter the no "))
        print("div ",x/y)
    elif op=="E":
        break

    else:
        print("wrong")   
