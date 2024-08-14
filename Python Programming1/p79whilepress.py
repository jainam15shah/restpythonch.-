while True:
    print("press 1 for squre")
    print("press 2 for cube")
    print("press 3 for exit")
    op=int(input("enter the op "))
    if op==1:
        x=int(input("enter the no "))
        print("squre ",x*x)
    elif op==2:
        x=int(input("enter the no "))
        print("cube ",x*x*x)
    elif op==3:
        break

    else:
        print("wrong")   
