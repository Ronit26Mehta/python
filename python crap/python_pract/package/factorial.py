def factorial(num):
    num3=1
    num1=0
    num2=1
    i=1
    while i<num:
       num3=num1+num2
       num1=num2
       num2=num3
       print(num2)
       i+=1
        
      
     