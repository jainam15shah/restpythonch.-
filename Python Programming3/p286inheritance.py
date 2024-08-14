class india:
    
    def __init__(self):
        self.a = 0
        
    def setindia(self):
        self.a = int(input("Enter the number "))
        
    def printindia(self):
        print("a =", self.a)

class usa(india):
    
    def __init__(self):
        self.b = 0
        
    def setusa(self):
        self.b = int(input("Enter the number "))
        
    def printusa(self):
        print("b =", self.b)
        
    def mul(self):
        print("a*b =", self.a * self.b)
u1=usa()
u1.setindia()
u1.setusa()
u1.printindia()
u1.printusa()
u1.mul()
