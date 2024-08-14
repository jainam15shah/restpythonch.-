t=int(input("enter the temperature "))
if t<0:
    print("freeezing atmosphere")
elif 0<=t<10:
    print("very cold atmosphere")
if 10<=t<20:
    print("cold atmosphere")
if 20<=t<30:
    print("normal atmosphere")
if 30<=t<40:
    print("hot atmosphere")
else:
    print("very hot atmosphere")