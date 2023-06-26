print("demonstration of aithemetic operator")
print("select form the given choice of operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.exponent")
print("6.floor")
print("7.modulos")
n=int(input("enter the choice:"))
if(n==1):
    num1=int(input("enter the  number 1:"))
    num2=int(input("enter the number2:"))
    num1+=num2
    print("take the result:",num1)
elif(n==2):
    num1=int(input("enter the  number 1:"))
    num2=int(input("enter the number2:"))
    num1-=num2
    print("take the result:",num1)
elif(n==3):
    num1=int(input("enter the  number 1:"))
    num2=int(input("enter the number2:"))
    num1*=num2
    print("take the result:",num1)
elif(n==4):
    num1=int(input("enter the  number 1:"))
    num2=int(input("enter the number2:"))
    num1/=num2
    print("take the result:",num1)
elif(n==5):
    num1=int(input("enter the  number 1:"))
    num2=int(input("enter the number2:"))
    num1**=num2
    print("take the result:",num1)
elif(n == 6):
    num1=int(input("enter the  number 1:"))
    num2=int(input("enter the number2:"))
    num1//=num2
    print("take the result:",num1)
elif(n == 7):
    num1=int(input("enter the  number 1:"))
    num2=int(input("enter the number2:"))
    num1%=num2
    print("take the result:",float(num1))
else:
    print("bong you entered the rat hole")
