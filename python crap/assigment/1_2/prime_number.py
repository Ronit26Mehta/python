n = int(input("enter the number to check prime "))
for i in range(2,n+1):
    if n % i == 0:
        break
if i == n:
    print("n is prime")
else:
    print("n is not a prime")
