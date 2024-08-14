f1=open("xyz","r")
f2=open("pqr","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        f2.write(ch.lower())
    elif ch.islower():
        f2.write(ch.upper())
    else:
        f2.write(ch.sort())
        pass 
    
    # if ch=="a" or ch=="e" or ch=="i"or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U":
    #     # pass
    #     f2.write(ch)
    # else:
    #     f3.write(ch)
    
f1.close()
f2.close()
print("copied")