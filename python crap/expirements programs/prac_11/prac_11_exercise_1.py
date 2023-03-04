def prime(x):
    if(x == 1):
        print(x,"is prime")
    elif(x == 2):
        print(x,"is prime")
    else:
        for m in range(2,x):
            if(x%m == 0):
                return False
        return True
x=int(input("enter the number"))
print("the false indicates not a prime")
print("the true indicates a prime")
print("the result is",prime(x))
