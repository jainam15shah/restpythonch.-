class stu:

    def __init__(self):
        self.sno=0
        self.sname=""
    def setstu(self):
        self.sno=int(input("enter the number "))
        self.sname=(input("enter the name "))
    def printstu(self):
        print("student number ",self.sno,"student name ",self.sname)
class marks(stu):

    def __init__(self):
        self.senglishmark=0
        self.shindimark=0
    def setmark(self):
        self.senglishmark=int(input("enter the eng mark "))
        self.shindimark=int(input("enter the hindi number "))
    def printmark(self):
        print("eng mark ",self.senglishmark,"hindi mark ",self.shindimark)

class result(marks):


    def printtotal(self):
        print("english + hindi marks= ",self.senglishmark + self.shindimark)

R1=result()
R1.setstu()
R1.setmark()
R1.printstu()
R1.printmark()
R1.printtotal()