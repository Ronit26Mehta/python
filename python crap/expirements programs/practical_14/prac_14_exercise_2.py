class Sqrrect:
   def area(self,l):
       print("the area of sqaure is:",l**2)
   def area(self,side=None,length=None,breadth=None):
        if(side!=None):
            res=side**2
            print("the area of sqaure is :",res)
        elif(length!=None and breadth!=None):
            print("the area of rectangle is:",lenght*breadth)
sqr=Sqrrect()
sqr.area(5)
sqr.area(4,65,7)
