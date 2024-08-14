def add(*a):
    print(sum(a))
    s1=0
    s2=0
    for x in a:
        if x%2==0:
            print(x,"is i1")
            s1=s1+x
        else:
            print(x,"is i2")
            s2=s2+x
    print("the sum of even number ", s1)
    print("the sum of odd number ", s2)
add(1,2,3,4,5,6)
add(12,33)
add(34,480,52,62)
7