def printer(num):
    n1=0
    n2=1
    n3=1
    i=1
    while i<num:
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
        i+=1