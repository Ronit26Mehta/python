num=int(input("enter the number to find the reverse"))
temp=num
rev=0
while temp!=0:
    rev=(rev*10)+(temp%10)
    temp=temp//10
if (num == rev):
    print("the entered number is palindrome")
    print(rev)
else :
    print("the entered number is not a palindrome")
    print(rev)

