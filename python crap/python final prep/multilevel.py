class base():
    def display(self):
        print("hello freind")
class base_actor(base):
    def display1(self):
        print("its pretty lame")
class derived(base_actor):
    def display2(self):
        print("maybe i should give you name")
d = derived()
d.display()
d.display1()
d.display2()