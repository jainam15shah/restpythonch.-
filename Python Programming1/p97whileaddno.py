s=0   
for i in range(1,6):
        no=int(input("enter the no."))
        if no>0:
            print(no)
            s=s+no
        else:
            print("wrong")
            break
                     
print("Sum = ",s)