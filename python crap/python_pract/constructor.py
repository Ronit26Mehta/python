class Construct():

    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary
    def printer(self):
        print("the name:",self.name)
        print("the salary:",self.salary)
        print("the department:",self.department)
c = Construct("ronit","department:co",100000)
c.printer()