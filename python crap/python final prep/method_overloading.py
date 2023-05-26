class area():
    def area_rect_sqaure(self,n1=None,n2=None):
        if n1 !=None and n2 !=None:
            print("the area of rectangle is:",n1*n2)
        elif n1 != None:
            print("the area of sqaure is:",n1*n1)
        else:
            print("no arguments passed")
a = area()
a.area_rect_sqaure(5)
a.area_rect_sqaure(5,10)