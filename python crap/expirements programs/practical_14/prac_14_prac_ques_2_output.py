class Animal:
    mutlicelluar = True
    eukrayotic = True
    def breathe(self):
        print("i breathe oxygen")
    def feed(self):
        print("i eat food")
class Herbivorous(Animal):
    def feed(self):
        print("i eat only plants.i am vegitarian")
herbi = Herbivorous()
herbi.feed()
herbi.breathe()
