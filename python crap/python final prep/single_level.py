class base():
    def display1(self):
        print("hello world")
class derived(base):
    def display2(self):
        print("hello freind")
d = derived()
d.display1()
d.display2()