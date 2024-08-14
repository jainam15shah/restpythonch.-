print("press D for Dosa")
print("press P for Pizza")
print("press B for Burger")
op=(input("enter opt =>")).upper()
if op=="D":
    x=int(input("enter the quantity =>"))
    print("prise od Dosa",x*100)
elif op=="P":
    x=int(input("enter the quantity =>"))
    print("prise of Pizza",x*200)
elif op=="B":
    x=int(input("enter the quantity =>"))
    print("prise of Burger",x*50)
else:
    print("wrong opt")

