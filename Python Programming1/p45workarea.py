A=int(input("enter the age "))
G=input("enter the gender ")
if G=="f":
    print("she will work only in urben areas ")
elif G=="m":
    if 20<=A<40:
        print("he may work in anywhere ") 
    elif 40<=A<60:
        print("he will work in urben areas only ")

else:
    print("error") 