print("set demonstration")
r=2
for i in range(r):
    i+=1
    r+=2
    print("1.adding")
    print("2.removing")
    print("3.exit")
    universal={0,}
    sets=set(universal)
    n=int(input("enter the choice"))
    
    if(n==1):
        elements=input("enter any element you want")
        sets.update([elements])
    elif(n==2):
        elements1=input("enter the elements to remove")
        sets.remove(elements1)
    elif(n==3):
        print(sets)
    else:
        print("you have been exited")
        print("the final result",sets)

    
#bong sets implementation
        
