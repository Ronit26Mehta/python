print("percentage finder")
num1=int(input("enter the marks for first subject"))
num2=int(input("enter the marks for second subject"))
num3=int(input("enter the marks for third subject"))
num4=int(input("enter the marks for fourth subject"))
num5=int(input("enter the marks for fifth subject"))
total=num1+num2+num3+num4+num5
avg=total/5
if(avg>=75):
    print("distinction")
elif(avg<75) and(avg>=60):
    print("first class")
elif(avg<60) and (avg>=50):
    print("second class")
elif(avg<50) and (avg>=40):
    print("just pass")
else:
    print("fail")
