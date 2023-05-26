class child():
    def read(self,name,id,roll):
        self.name=name
        self.id=id
        self.roll=roll
    def printer(self):
        print("the name:",self.name)
        print("the id:",self.id)
        print("the roll:",self.roll)
name1=str(input("enter the value to display(name):"))
id=int(input("enter the value to display(id):"))
roll = int(input("enter the value to display(roll)"))
c = child()
c.read(name1,id,roll)
c.printer()