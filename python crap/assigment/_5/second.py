class Employee:
    Id=0
    name = ""
    def read(self):
        self.Id=int(input("enter the Id:"))
        self.name=str(input("enter the name:"))
    def printer(self):
        print("the Id is :",self.Id)
        print("the name is:",self.name)
e = Employee()
e.read()
e.printer()
