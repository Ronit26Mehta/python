def factor(num):
    count=1
    if(num>0):
       for i in range(1,num+1):
           count*=i
    else:
        print("negative numbers like this= %d(are not allowed)" %(num) )
    return count
num=int(input("enter the number"))
print("the facotrial is ",factor(num))
