class Calculator:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
    def add(self):
        print("add", self.num1 + self.num2)

Obj1= Calculator(4,5)
Obj1.add()

