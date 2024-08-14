f1=open("abc","r")
s1=0
s2=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        pass
    elif ch.islower():
        s1+=1
    else:
        s2+=1
    
f1.close()
print("the total lower is ",s1)
print("the total other is ",s2)
