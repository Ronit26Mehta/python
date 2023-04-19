class Employee:
    name= ""
    department = ""
    salary = 0
    def read(self):
        self.name = str(input("enter the name"))
        self.department=str(input("enter the department"))
        self.salary= int(input("enter the salary"))
    def printer(self):
        print("the name is :",self.name)
        print("the department is :",self.department)
        print("the salary is:",self.salary)
e = Employee()
e.read()
e.printer()
