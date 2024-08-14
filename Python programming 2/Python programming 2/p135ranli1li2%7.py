import random

n = int(input("Enter the limit: "))
l1 = []
l2 = []  
  

for i in range(1, n + 1):
    y = random.randint(1,50)
    l1.append(y)

for x in l1:
    if x % 7 == 0:
        l2.append(x)
    else:
        pass
        

print("List of divtion by seven:", l2)
