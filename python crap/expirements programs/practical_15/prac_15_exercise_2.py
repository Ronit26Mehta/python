class Student:
    def Reading(self,name=chr,department=chr,rollno=int,marks=float):
        self.name=name
        self.department=department
        self.rollno=rollno
        self.marks=marks
class print1(Student):
    def printing(self):
        print("the name is:",self.name)
        print("the department is:",self.department)
        print("the roll no. is:",self.rollno)
        print("the marks is:",self.marks)
pr = print1()
pr.Reading("ronit","co",72,91.67)
pr.printing()

