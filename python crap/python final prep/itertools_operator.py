from itertools import chain
from itertools import cycle
def chainer():
    for i in chain([10,20,30],["python","java","c++"]):
        print(i)
def cycler():
    index=0
    for i in cycle(["hello world"]):
        index+=1
        print(i)
        if index == 10:
            break
chainer()
cycler()