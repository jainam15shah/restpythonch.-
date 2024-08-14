print("press 1 for squre")
print("press 2 for cube")
op=int(input("enter opt =>"))
if op==1:
    y=int(input("enter number =>"))
    print("squre", y*y)
elif op==2:
    y=int(input("enter number =>"))
    print("cube", y*y*y)
else:
    print("wrong call")
