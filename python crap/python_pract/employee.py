class Empolyee():
    name=""
    department=""
    salary=0
    def reading(self):
        self.name=str(input("enter name:"))
        self.department=str(input("enter department:"))
        self.salary=int(input("enter salary:"))
    def printer(self):
        print("the name is:",self.name)
        print("the department is:",self.department)
        print("the salary is:",self.salary)
e = Empolyee()
e.reading()
e.printer()