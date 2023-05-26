n = int(input("enter the number to check for prime:"))
for i in range(2,n+1):
    if (n % i )== 0:
        break
if i == n:
    print("prime")
else:
    print("not a prime")