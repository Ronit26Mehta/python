class a:
    def d1(self):
        print("this is class a")
class b:
    def d2(self):
        print("this is class b")
class c(a,b):
    def d3(self):
        print("this is class c")
n1=c()
n1.d1()
n1.d2()
n1.d3()
