class Empolyee:
    def Reading(self,name=chr,department=chr,salary=int):
        self.name=name
        self.department=department
        self.salary=salary
class print1(Empolyee):
    def printing(self):
        print("the name is:",self.name)
        print("the department is:",self.department)
        print("the salary is:",self.salary)
pr = print1()
pr.Reading("ronit","lead",50000)

pr.printing()
pr.Reading("r","lead",50000)
pr.printing()
