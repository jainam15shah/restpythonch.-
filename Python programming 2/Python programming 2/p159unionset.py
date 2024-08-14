import random
y=7
set1=set()

for i in range(1,y+1):
    n=random.randint(1,30)
    set1.add(n)
print(set1)

set2=set()

for i in range(1,y+1):
    n=random.randint(1,30)
    set2.add(n)
print(set2)

print(set1.isunionset(set2))

