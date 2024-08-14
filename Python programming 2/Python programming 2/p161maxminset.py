import random
y=7
set1=set()

for i in range(1,y+1):
    n=random.randint(1,30)
    set1.add(n)
print(set1)
print("min value",min(set1))
print("max value",max(set1))
