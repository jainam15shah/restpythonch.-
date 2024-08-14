import random
x=random.randint(1,30)
y=random.randint(1,30)
print("no1= ",x,"no2= ",y)
z=int(input("enter add=>"))
if z==x+y:
    print("right ans")
else:
    print("wrong ans")