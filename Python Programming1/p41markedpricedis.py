p=int(input("enter the price "))
if p>10000:
    d=p*0.2
    print("with discount",p-d)
elif 7000<p<=1000:
    d=p*1.5
    print("with discount",p-d)
else:
    d=p*0.1
    print("with discount",p-d)
