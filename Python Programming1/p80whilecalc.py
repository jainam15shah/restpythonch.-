while True:
    print("press 1 for add")
    print("press 2 for sub")
    print("press 3 for mul")
    print("press 4 for div")
    print("press 5 for exit")
    op=int(input("enter the op "))
    if op==1:
        x=int(input("enter the no "))
        y=int(input("enter the no "))
        print("add ",x+y)
    elif op==2:
        x=int(input("enter the no "))
        y=int(input("enter the no "))
        print("sub ",x-y)
    elif op==3:
        x=int(input("enter the no "))
        y=int(input("enter the no "))
        print("mul ",x*y)
    elif op==4:
        x=int(input("enter the no "))
        y=int(input("enter the no "))
        print("div ",x/y)
    elif op==5:
        break

    else:
        print("wrong")   
