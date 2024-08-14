f1=open("abc","r")
s=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch=="a" or ch=="e" or ch=="i"or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U":
        s+=1
f1.close()
print("the total vowel is ",s)