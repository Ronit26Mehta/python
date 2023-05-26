letter = str(input("enter the characters to check for file:"))
counter = 0
with open("f2.txt",'r+') as input:
    for i in input.read():
        str1 = i.split()
        for j in str1:
            if j == letter:
                counter+=1
print("the occurences of {}".format(letter))
print(counter)