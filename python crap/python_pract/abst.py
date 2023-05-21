class abst:
    a = 10
    __b=10
    def public_method(self):
        print("main functionallity")
        print("a=",self.a)
        return self.__b
        
    def __private_method(self):
        print("private method")
        return self.__b
ab = abst()
ab.public_method()