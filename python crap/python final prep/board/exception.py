n = int(input("enter any number to divide it:"))
num1 = int(input("enter the number"))
try:
       answer = num1/n
       print(answer)
except ZeroDivisionError:
    print("not possible zero divison error")
else:
    print("program executed")
