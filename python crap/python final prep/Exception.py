num1 = int(input("enter the number one:"))
num2 = int(input("enter the number two:"))
try:
    result=num1/num2
    print("the result is:",result)
except ZeroDivisionError:
    print("zero division not possible")
except ArithmeticError:
    print("arithmetic error has been caused")
except FloatingPointError:
    print("caused due to illegal floating point exceeding")
else:
    result = num1/num2
    print("the result is:",result)