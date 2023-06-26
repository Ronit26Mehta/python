n1=int(input("enter the number1 "))
n2=int(input("enter the number2"))
try:
    result=n1/n2
except ZeroDivisionError:
        print("the result is not possible as division by zero")
else:
  print("the result:",result)
finally:
    print("the program executed successfully")
