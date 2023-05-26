class Empolyee:
    name=""
    roll=0
    branch=""
    def read_data(self,name,roll,branch):
        self.name=name
        self.roll=roll
        self.branch=branch
    def print_data(self):
        print("the name is:",self.name)
        print("the branch is :",self.branch)
        print("the salary is:",self.roll)
def iterator():
    value = True
    while value == True:
        n1= input("enter the name")
        n2 = input("enter the branch")
        n3 = input("enter the salary")
        e = Empolyee()
        e.read_data(n1,n2,n3)
        e.print_data()
iterator()