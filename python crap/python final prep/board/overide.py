class Animal():
    def breathe(self):
        print("i breathe oxygen")
    def feed(self):
        print("i eat food")
class Herbivours(Animal):
    def feed(self):
        print("i eat grass")
h = Herbivours()
h.feed()
h.breathe()
a = Animal()
a.feed()
a.breathe()