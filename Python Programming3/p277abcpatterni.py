# Left triangle pattern
n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(i + 97), end="")
    print()