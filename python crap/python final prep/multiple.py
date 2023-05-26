class multiplier():
    def display1(self):
        print("hello world")
class mult():
    def display2(self):
        print("hello freind")
class derived(multiplier,mult):
    def display3(self):
        print("hello dude")
d = derived()
d.display1()
d.display2()
d.display3()