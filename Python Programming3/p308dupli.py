l1=[5,66,22,45,32,15,5,15,5,22]
l2=[]
for x in l1:
    if l2.count(x)>0:
        pass
    else:
        l2.append(x)

print(l2)
        
for x in l2:
    print(x,l1.count(x))