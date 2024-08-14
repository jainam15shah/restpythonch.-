while True:
    print("press s for squre")
    print("press c for cube")
    print("press E for exit")
    op=(input("enter the op "))
    if op=="s":
        x=int(input("enter the no "))
        print("squre ",x*x)
    elif op=="c":
        x=int(input("enter the no "))
        print("cube ",x*x*x)
    elif op=="E":
        break

    else:
        print("wrong")   
