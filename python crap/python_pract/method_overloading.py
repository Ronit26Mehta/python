class Overloading():
    def function(self,l=None,b=None):
        if(l!=None and b!=None):
            return l*b
        elif(l!=None):
            return l*l
        else:
            return "the parameters were not passed"
o = Overloading()
print(o.function(10,2))
print(o.function(7))
print(o.function())