import operator
d ={1:2,3:4,4:3,2:1,0:0}
print('original dictionary:' , d)
sort_a=sorted(d.items(), key = operator.itemgetter(1))
sort_d=dict(sorted(d.items(),key = operator.itemgetter(1),reverse = True))
print("ascedning order",sort_a)
print("descending order",sort_d)
