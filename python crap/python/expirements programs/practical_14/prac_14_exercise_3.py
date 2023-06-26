class Degree:
    def getDegree(self):
        print("i got a degree")
class Undergraduate(Degree):
    def getDegree(self):
        print("i am a undergraduate")
class Postgraduate(Degree):
    def getDegree(self):
        print("i am a postgraduate")
deg =Degree()
deg.getDegree()
undgrad = Undergraduate()
undgrad.getDegree()
postgrad = Postgraduate()
postgrad.getDegree()
