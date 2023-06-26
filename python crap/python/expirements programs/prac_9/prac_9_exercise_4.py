dic1=[{"v":"S001"},{"v":"S002"},{"vi":"S001"},{"vi":"S005"},{"vii":"S005"},{"v":"S009"},{"viii":"S007"}]
print("the original list :" +str(dic1))
res = list(set(val for dic in dic1 for val in dic.values()))
print("the unique values in the list are:" + str(res))
