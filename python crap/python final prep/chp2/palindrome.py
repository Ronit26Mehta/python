n = int(input("enter the number to check for palindrome:"))
rev = 0
rem = n
while(rem>0):
    rev = (rev*10)+(rem%10)
    rem = rem //10
    
if n == rev:
    print("palindrome",rev)
else:
    print(" not a palindrome")

