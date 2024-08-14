import random

n = int(input("Enter the limit: "))
l1 = []

for i in range(1, n + 1):
    y = random.randint(-10, 20)
    l1.append(y)

print(l1)

print("After\n")
for x in l1:
    print(x*-1,",", end = " ")