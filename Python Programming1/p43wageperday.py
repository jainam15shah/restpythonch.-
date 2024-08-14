A=int(input("enter the age "))
if 18<=A<30:
   G=input("enter the gender ")
   if G=="m":
      print("the wage/day is 700")
   elif G=="f":
       print("the wage/day is 750")
   else:
    print("enter the wrong gender ")       
elif 30<=A<40:
    G=input("enter the gender ")
    if G=="m":
      print("the wage/day is 800")
    elif G=="f":
       print("the wage/day is 850")
    else:
     print("enter the wrong gender ")       


else:
    print("this is below age ")       
      
