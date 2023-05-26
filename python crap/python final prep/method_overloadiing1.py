class mehtod_overloader():
    def addition(self,n1=None,n2=None):
        if n1 !=None and n2 !=None:
            print("the value of addition is:",n1+n2)
m = mehtod_overloader()
m.addition(10,2)
m.addition("hello","freind")
m.addition(2.0,5.6)
m.addition(2+5j,3+8.9j)
m.addition([10,20,30,40,50],[60,70,80,90])
m.addition((10,20,30,40,50),(60,70,80,90))

