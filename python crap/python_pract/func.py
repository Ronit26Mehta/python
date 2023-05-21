#user defined function example
def func(num):
    total=1
    for i in range(1,num+1):
        total*=i
    print(total)
func(6)