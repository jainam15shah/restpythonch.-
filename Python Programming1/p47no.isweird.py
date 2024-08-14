n=int(input("enter the number "))
if n%2==0:
    print("the no is even")
    if 2<=n<=5:
        print("not weird")
    elif 6<=n<=20:
        print("weird")
    elif n>20:
        print("not weird")
    else:
        print("not a mension no")


else:
    print("weird")

