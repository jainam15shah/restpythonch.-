u=int(input("enter the number of unit "))
if u<=100:
    print("total amount to pay is",(u*0))
elif 101<=u<=300:
    print("total amount to pay is",((u-100)*2))
else:
    print("total amount to pay is",((u-300)*5))
    
    