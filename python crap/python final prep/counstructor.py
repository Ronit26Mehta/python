class construct():
    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print("the object has been created")
    def area(self):
        print("the area of rect",self.num1*self.num2)
        print("the area of sqaure",self.num3*self.num3)
c = construct(10,20,3)
c.area()
