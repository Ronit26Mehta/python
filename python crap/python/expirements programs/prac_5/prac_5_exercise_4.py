count=0
nterms=int(input("enter the number of terms"))
num1=0
num2=1
while count<nterms:
    print(num1)
    nthterm=num1+num2
    num1=num2
    num2=nthterm
    count+=1
