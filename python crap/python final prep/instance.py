class variable:
    x = 10
    def instance(self,y):
        self.y=y
        print(y)
c = variable()
c.instance(10)
c.x=11
print(c.x)
s = variable()
print(s.x)
