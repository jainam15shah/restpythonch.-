print("press s for squre")
print("press c for cube")
op=(input("enter opt =>"))
if op=="s" or op=="S":
    y=int(input("enter number =>"))
    print("squre", y*y)
elif op=="c":
    y=int(input("enter number =>"))
    print("cube", y*y*y)
else:
    print("wrong call")
