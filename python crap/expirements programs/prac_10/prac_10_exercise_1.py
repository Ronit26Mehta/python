print("string checker")
n=str(input("enter the string:-"))
n1=0
n2=0
for i in n:
    if(i.isupper()):
        n1+=1
    if(i.islower()):
        n2+=1
print("the upper case character:-",n1)
print("the lower case character:-",n2)
