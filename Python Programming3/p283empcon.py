class emp:
    def __init__(self):
        self.eno=0
        self.ename=""
        self.salary=0
    def printdata(self):
        print("eno= ", self.eno,"name= ", self.ename,"salary= ", self.salary)
    def setdata(self):
        self.eno=int(input("enter the number "))
        self.ename=input("enter the name ")
        self.salary=int(input("enter the ctc "))
e1=emp()
e2=emp()
e3=emp()
e1.setdata()
e2.setdata()
e3.setdata()
e1.printdata()
e2.printdata()
e3.printdata()