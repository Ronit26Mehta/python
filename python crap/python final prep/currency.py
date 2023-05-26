def dollar_inr():
    n = int(input("enter the number of dollar to be coneverted inr:"))
    converter = n*80
    print("the result is:",converter)
def euro_inr():
    n = int(input("enter the inr"))
    converter=n*85
    print("the result is:",converter)
def menu():
    value = True
    while value == True:
        print("enter 1 to convert to usd")
        print("enter 2 to convert to euro")
        print("enter 3 to exit") 
        n = int(input("enter the choice"))
        if n == 1:
            dollar_inr()
        elif n == 2:
            euro_inr()
        elif n == 3:
            value = False
        else:
            print("enter the correct option") 
menu()                                                                                                                                             