f1=open("abc","r")
s=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch==" ":
        s+=1
f1.close()
print("Total spaces are ",s)