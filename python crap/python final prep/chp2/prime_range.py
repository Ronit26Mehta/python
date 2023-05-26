n = int(input("enter the start:"))
e = int(input("enter the end"))
for i in range(n,e+1):
    for j in range(2,i):
        if i % j == 0:
            break
        else:
            print(i)
    
    
