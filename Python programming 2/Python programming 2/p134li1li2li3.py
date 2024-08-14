import random

n = int(input("Enter the limit: "))
l1 = []
l2 = []  # List for even numbers
l3 = []  # List for odd numbers

for i in range(1, n + 1):
    y = random.randint(1, 30)
    l1.append(y)

for x in l1:
    if x%2==0:
        l2.append(x)
    else:
        l3.append(x)
 
print("List of even numbers:", l2)
print("List of odd numbers:", l3)
