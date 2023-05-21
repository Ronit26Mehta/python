num1 = 10
num2=0
try:
    qou=num1/num2
    print(qou)
except ZeroDivisionError:
    print("the division is not possible")
else:
    qou = num1/num2
    print(qou)
