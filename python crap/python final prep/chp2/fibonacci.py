n = int(input("enter the number to generate fibonacci:"))
n1 = 0
n2 = 1
n3 = 1
i = 1
while i<n:
    n3 = n2 + n1
    n1 = n2
    n2 = n3 
    print(n3)
    i += 1
