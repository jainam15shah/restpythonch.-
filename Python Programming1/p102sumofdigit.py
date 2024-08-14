num=int(input("enter the number"))
y=num
sum=0
while num>0:
    digit = num % 10
    sum=sum+digit
    num //= 10

print("sum of the digit: ",sum)