with open("f1.txt","+r") as input:
    with open("f2.txt","+w") as output:
        for i in input:
            output.write(i)