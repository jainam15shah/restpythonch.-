m=int(input("enter the month "))
y=int(input("enter the year "))
if m==2:
    y=int(input("enter the year "))
    if y%2==0:
        print("feb has 29 days",y)
    else:
        print("feb has 28 days",y)
elif m==1:
    print("jan has 31 days",y)
elif m==3:
       print("march has 31 days",y)
elif m==4:
        print("apr has 30 days",y)
elif m==5:
        print("may has 31 days",y)
elif m==6:
        print("jun has 30 days",y)
elif m==7:
        print("jul has 31 days",y)
elif m==8:
        print("aug has 31 days",y)
elif m==9:
        print("sep has 30 days",y)
elif m==10:
        print("oct has 31 days",y)
elif m==11:
        print("nov has 30 days",y)
elif m==12:
        print("dec has 31 days",y)
else:
    print("wrong number")