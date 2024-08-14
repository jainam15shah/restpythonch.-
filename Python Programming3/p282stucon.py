class stu:
    def __init__(self):
        self.sno=0
        self.name=""
        self.english=0
        self.hindi=0
    def printdata(self):
        print("sno= ", self.sno," name= ",self.sname," english= ",self.english," hindi= ",self.hindi)
    def setdata(self):
        self.sno=int(input("enter the number "))
        self.sname=input("enter the name ")
        self.english=int(input("enter the mark "))
        self.hindi=int(input("enter the mark "))
s1=stu()
s2=stu()
s3=stu()
s4=stu()
s1.setdata()
s2.setdata()
s3.setdata()
s4.setdata()
s1.printdata()
s2.printdata()
s3.printdata()
s4.printdata()
