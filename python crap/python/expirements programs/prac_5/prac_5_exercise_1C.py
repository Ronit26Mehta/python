no =5
for m in range (no-1,0,-1):
    for n in range(no,m,-1):
        print(" ",end='')
    for l in range(2*m-1,0,-1):
        if(l%2!=0):
            print("1",end='')
            
        else:
            print("0",end='')
    print()
