import random

n = int(input("Enter the limit: "))
l1 = []

for i in range(1, n + 1):
    y = random.randint(1, 30)
    l1.append(y)

print("Generated list:", l1)

# Calculate max and min values after the loop
max(l1)
min(l1)

print("Max value:", max(l1))
print("Min value:", min(l1))
