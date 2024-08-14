# num = int(input("Enter the number:"))
# y=num
# reversed_num = 0

# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10

# print("Reversed Number: ",(reversed_num))
# print("no: ",(y))
# if reversed_num==y:
#     print("palindrome")
# else:
#     print("not a palindrome")    
s=(input("enter "))
revstr=(s[:2:-1])
if revstr==s:
    print("palindrome")
else:
    print("not a palindrome")    
