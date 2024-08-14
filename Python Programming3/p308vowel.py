f1=open("bcd","r")
f2=open("efg","w")

while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch=="a" or ch=="e" or ch=="i"or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U":
        f2.write(ch)
        pass
f1.close()
f2.close()
