tuple1 = (10,20,30)
tuple2 = (20,30,40)
print("the tuple before changing")
print("the tuple 1 :", tuple1)
print("the tuple 2:", tuple2)
list1 = list(tuple1)
list2 = list (tuple2)
list3=list1
list1=list2
list2=list3
tuple1 = tuple(list1)
tuple2 = tuple(list2)
print("the tuple after changing")
print("the tuple 1 : ", tuple1)
print("the tuple 2 :", tuple2)
