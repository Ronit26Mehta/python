print("the common")
l=[10,230,450,12,2,4]
r=[2,3,4,230,10,20,5]
f=[]
for i in l:
    for m in r:
        if(i == m):
            f.append(i)
            
print("the common element are:",f)
