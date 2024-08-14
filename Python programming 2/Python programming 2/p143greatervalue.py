import random

n = int(input("Enter the limit: "))
l1 = []
y=int(input("enter greater than value "))
for i in range(1,n + 1):
    y = random.randint(1, 30)
    l1.append(y)
    print(l1)

for x in l1:
    
    if x>y:
        print(x)