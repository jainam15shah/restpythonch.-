# f1=open("abc","r")
# s1=0
# s2=0
# s3=0
# s4=0
# while True:
#     ch=f1.read(1)
#     if not ch:
#         break
#     if ch.isupper():
#         s1+=1
#     elif ch.islower():
#         s2+=1
#     elif ch in "aeiouAEIOU":
#         s3+=1
#         print(" 7 ",end="")
#     else:
#         s4+=1
    
# f1.close()

# print("the total upper is ",s1)
# print("the total lower is ",s2)
# print("the total vowel is ",s3)
# print("the total other is ",s4)
f1 = open("abc", "r")
s1 = 0
s2 = 0
s3 = 0
s4 = 0
while True:
    ch = f1.read(1)
    if not ch:
        break
    if ch.isupper():
        s1 += 1
    elif ch.islower():
        s2 += 1
    if ch=="aeiouAEIOU":
        print("7 ",end="")
        
        s3 += 1
    else:
        s4 += 1

f1.close()

print("the total upper is ", s1)
print("the total lower is ", s2)
print("the total 7 is ", s3)
print("the total other is ", s4)
