class animal():
    def feed(self):
        print("i eat food")
class heribivourous(animal):
    def feed(self):
        print("i eat only grass")
h = heribivourous()
h.feed()
a = animal()
a.feed()