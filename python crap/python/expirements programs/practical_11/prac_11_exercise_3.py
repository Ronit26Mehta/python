def string(st):
    n1=0
    n2=0
    for i in st:
        if(i.isupper()):
            n1+=1
        elif(i.islower()):
            n2+=1
    
    print("the upper case is:",n1)
    print("the lower case is:",n2)
st=str(input("enter the string"))

