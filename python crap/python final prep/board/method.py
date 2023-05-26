class method():
    def area(self,num1=None,num2=None):
        if num1 !=None and num2 !=None:
            return num1 * num2
        elif num1 != None:
            return num1 * num1
        else:
            return " send the arguments"
m = method()
print(m.area(10,60))
print(m.area(10))
print(m.area())