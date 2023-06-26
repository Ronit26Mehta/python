print("welcome to percentage finder")
print("enter seqeuntially marks of five subjects")
m1=int(input("enter the marks of the first subject"))
m2=int(input("enter the marks of the second subject"))
m3=int(input("enter the marks of the third subject"))
m4=int(input("enter the marks of the fourth subject"))
m5=int(input("enter the marks of the fifth subject"))
total=m1+m2+m3+m4+m5
average=total/5
if (average>=75):
    print("distinction")
elif (average<=74) and (average>=60):
    print("first class")
elif(average<=59) and (average>=40):
    print("second class")
else:
    print("fail")
