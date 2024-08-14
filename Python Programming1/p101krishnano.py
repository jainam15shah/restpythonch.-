import math

num = int(input("Enter the number:"))
y = num
sum = 0

while num > 0:
    digit = num % 10
    sum += math.factorial(digit)
    num //= 10

if sum == y:
    print("Krishnamurthy number")
else:
    print("Not a Krishnamurthy number")
