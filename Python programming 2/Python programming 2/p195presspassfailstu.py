import random
d1={}
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    no=i
    mark=random.randint(1,40)
    d1[no]=mark

print(d1)
while True:
    print("press 1 for pass student ")
    print("press 2 for fail student ")
    print("press 3 for whole recorde ")
    op=int(input("enter the opt"))
    if op==1:

        print("no\tmark\tresult")
        print("*"*30)
        for k,v in d1.items():
            if v>=18:
                print(k,"\t",v,"\tPass")
                
        print("*"*30)
    elif op==2:
        print("no\tmark\tresult")
        print("*"*30)
        for k,v in d1.items():
            if v<=18:
                print(k,"\t",v,"\tfail")

        print("*"*30)


    elif op==3:
        c1=0
        c2=0
        print("no\tmark\tresult")
        print("*"*30)

        for k,v in d1.items():
            if v>=18:
                print(k,"\t",v,"\tPass")
                c1=c1+1
        
            else:
                print(k,"\t",v,"\tfail")
                c2=c2+1
        print("pass",c1)
        print("fail",c2)
        print("*"*30)
    else:
        print("wrong opt") 
        break   
    
    
    
    