class dest():
    def __init__(self):
        print("constructor created")
    def printer(self):
        print("in the midway")
    def __del__(self):
        print("the object has been destroyed")
d = dest()
d.printer()
del d 