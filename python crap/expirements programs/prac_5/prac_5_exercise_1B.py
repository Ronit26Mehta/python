no =int(input("enter the number of stars"))
for m in range(0,no):
    for n in range(0,no-m-1):
        print( " ",end='')
    for l in range(0,2*m+1):
        print("*",end='')
    print()
for m in range (no-1,0,-1):
    for n in range(no,m,-1):
        print(" ",end='')
    for l in range(2*m-1,0,-1):
        print("*",end='')
    print()
