import random

n = int(input("Enter the limit: "))
l1 = []

for i in range(1,n + 1):
    y = random.randint(1, 30)
    l1.append(y)
    print(l1)
    l1.insert(int(input("enter the position ")),int(input("enter the value ")))
    
    print(l1)