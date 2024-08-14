f1=open("abc","r")
s1=0
s2=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        s1+=1
    elif ch.islower():
        s2+=1

f1.close()
print("the total upper is ",s1)
print("the total lower is ",s2)