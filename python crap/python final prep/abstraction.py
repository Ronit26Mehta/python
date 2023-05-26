class abstract():
    b = 10
    __a=20
    def __private_method(self):
        print("private method")
    def public_method(self):
        print("public method")
        print("the value of private a",self.__a)
        self.__private_method()
        print("the value of b is:",self.b)
a = abstract()
a.public_method()
print(a.b)