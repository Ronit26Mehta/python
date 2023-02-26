set1={1,2,3,4,6,8}
set2={1,2,3,4,5}
set3={0}
set(set1)
set(set2)
set(set3)
print(set1)
print(set2)
print("intersection:-",set3.intersection(set1,set2))
print("union:-",set3.union(set1,set2))
print("difference",set1.difference(set2))
print("the symmetric difference",set1.symmetric_difference(set2))
print("before clear",set1)
print("after clear",set1.clear())
