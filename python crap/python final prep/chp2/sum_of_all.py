n = int(input("enter the number:"))
sum1 = 0
real_num=n
while (real_num>0):
    sum1 = sum1 + (real_num%10)
    real_num=real_num//10
print("the sum is:",sum1) 