print("press D for Dosa")
print("press P for Pizza")
print("press B for Burger")
op=(input("enter opt =>")).upper()
if op=="D":
    x=int(input("enter the quantity =>"))
    if x==1:
       print("prize of Dosa",x*100)
    else:
       print("the dosa is buy 2 get 1 free",(x+1))
       print("prize of Dosa",x*100)

elif op=="P":
    x=int(input("enter the quantity =>"))
    if x<=2:
       print("prize of Pizza",x*200)
    else:
       print("the Pizza is buy 3 get 1 free",(x+1))
       print("prize of Pizza",x*200)

elif op=="B":
    x=int(input("enter the quantity =>"))
    if x==1:
       print("prize of Burger ",x*50)
    else:
       print("the Burger is buy 2 get 1 free",x+1)
       print("prize of Burger",x*50)


else:
    print("wrong opt")

