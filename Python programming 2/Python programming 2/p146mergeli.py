import random

n = int(input("Enter the limit: "))
l1,l2 = [],[]
for i in range(1,n + 1):
    y = random.randint(1, 30)
    l1.append(y)
for i in range(1,n + 1):
    y = random.randint(1, 30)
    l2.append(y)
    print(l2)
    
print("mege list",l1+l2)
    