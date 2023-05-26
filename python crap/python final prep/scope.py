a = 10 #global variable
def scoper():
    b = 20 #local variable
    print(a)
    print(b)
scoper()
