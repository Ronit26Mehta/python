number_of_lines=int(input("enter the lines to write"))
str1 = ""
l1 = []
for i in range(1,number_of_lines+1):
    str1 = str(input("enter the content"))
    string = str1+"\n"
    l1.append(string)
n = int(input("enter the last lines"))
str2=""
l2=[]
for i in range(1,n+1):
    str2 = str(input("enter the content"))
    string2= str2+"\n"
    l2.append(string2)
with open("f2.txt","+w") as input:
    for i in range(1,number_of_lines+1):
        input.writelines(l1)
       
with open("f2.txt","+a") as append:
    for i in range(1,n+1):
        append.writelines(l2)
        
 
    