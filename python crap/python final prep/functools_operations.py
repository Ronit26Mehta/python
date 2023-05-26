from functools import partial
def mulitply(x,y):
    return x * y
double = partial(mulitply,y=3)
tripple = partial(mulitply,y=2)
print("the value of the tripple",tripple(5))
print("the value of the double",double(5))