n = 10
def funct():
    n2 = 20
    print("the local variable:",n2)
    print("the global variable:",n)
#print(n2) # local variables are not accessible
print(n)
funct()