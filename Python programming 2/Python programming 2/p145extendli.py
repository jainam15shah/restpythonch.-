import random

n = int(input("Enter the limit: "))
l1 = []
l2 = []
for i in range(1,n + 1):
    y = random.randint(1, 30)
    l1.append(y)
    l2.append(y)
    print(l1)
    print(l2)
    l1.extend(l2)
    print(l1)