import random

n = int(input("Enter the limit: "))
l1 = []
s=0

for i in range(1, n + 1):
    y = random.randint(1, 30)
    l1.append(y)
    s=s+y
    print(l1)
print("sum ",s)