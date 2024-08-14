num = int(input("Enter the number:"))
y=num
armstrong_num = 0

while num != 0:
    digit = num % 10
    armstrong_num = armstrong_num + digit * digit * digit
    num //= 10

print("armstrong num: ",(armstrong_num))
print("no: ",(y))
if armstrong_num==y:
    print("armstrong")
else:
    print("not a armstrong")    
