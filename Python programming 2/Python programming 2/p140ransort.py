import random

n = int(input("Enter the limit: "))
l1 = []

for i in range(1,n + 1):
    y = random.randint(1, 30)
    l1.append(y)
    print(l1)
    l1.sort()
    print("ascending order ",l1)
    l1.reverse()
    print("descending order ",l1)