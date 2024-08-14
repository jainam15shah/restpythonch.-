class math:
    def __init__(self):
        # print in the bracket self
        self.a=0
        self.b=0
    def setdata(self):
        self.a=int(input("enter the number "))
        self.b=int(input("enter the number "))
    def printdata(self):
        print("a=",self.a,"b=",self.b)
    def add(self):
        print("add=",self.a+self.b)
    def sub(self):
        print("sub=",self.a-self.b)
    def mul(self):
        print("mul=",self.a*self.b)
    def div(self):
        print("div=",self.a/self.b)


m1=math()
m1.setdata()
m1.printdata()
m1.add()
m1.sub()
m1.mul()
m1.div()