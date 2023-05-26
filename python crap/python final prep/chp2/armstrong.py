n = int(input("enter the number:"))

num_1=n
sum1=0
while (n>0):
       rem = n%10
       sum1= sum1+rem*rem*rem
       n= n//10

if num_1 == sum1:
    print("amrstrong number")
else:
    print("not an armstrong number")