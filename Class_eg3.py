class Teacher:
    def __init__(self,name,reg_no):
        self.name = name
        self.reg_no = reg_no
    def display(self):
        print("Name: ", self.name)
        print("Reg_no: ", self.reg_no)
T1 = Teacher("Akil", "1")
T1.display()
T2 = Teacher("Avi", "2")
T2.display()