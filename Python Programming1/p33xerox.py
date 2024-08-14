print("xerox shope")
print("press")
xeroxpages=int(input("enter the number =>"))
colorpages=int(input("enter the number =>"))
if xeroxpages<50:
    print("the prise is 5 rupees per page",xeroxpages*5)
elif  xeroxpages>=50:
    print("the prise is 3 rupees per page",xeroxpages*3)
else:
    print("the prise is 10 rupees per page",xeroxpages*10)

