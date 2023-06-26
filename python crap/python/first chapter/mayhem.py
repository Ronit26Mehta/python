print("enter the mayhem")
elements=[10,0,20,30,60]
n=bytes(elements)
guess=int(input("enter the given number position for 10"))
if(n[guess]==10):
    print("welcome to mayhem")
    result=n[0]+n[1]+n[2]+n[3]+n[4]
    print("the mayhem ends",result)
else:
    print("you picked the wrong house fool")
    print("your selection:-")
    print(n[guess])
    print("get rekt")
    print(n*5)

"""welcome to mayhem program
this the end"""
