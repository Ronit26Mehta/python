print("another dumb calcutor for cylinder ")
radius=int( input("enter the radius of the cylinder"))
print("select from the given option:-")
print("0.3.14 for pi")
print("1.22/7 for pi")
choice=bool(input("enter the choice:-"))
if(choice==0):
        pi=3.14
        resultar=2*pi*radius
        resultpr=pi*radius*radius
        print("frist:",resultar)
        print("second:",resultpr)

else:
        pi=22/7
        resultar=2*pi*radius
        resultpr=pi*radius*radius
        print("frist:",resultar)
        print("second:",resultpr)
