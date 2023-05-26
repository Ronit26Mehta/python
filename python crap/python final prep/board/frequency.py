n = input("enter the character")
count = 0
with open("f1.txt","+r") as input:
    for i in input.read():
        string = i.split()
        for j in string:
            if j == n:
                count+=1
print("the count of the characters is:",count)

