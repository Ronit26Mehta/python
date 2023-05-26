n = int(input("enter the lines to be written"))
l = []
for i in range(1,n+1):
    read = str(input("enter content"))
    l.append(read)


with open("f1.txt",'+w') as input:
    for i in range(1,n+1):
        input.writelines(l)
        input.write("\n")


with open("f1.txt",'+r') as input:
    with open("f2.txt","+w") as output:
        for i in input:
            output.write(i)
            output.write("\n")