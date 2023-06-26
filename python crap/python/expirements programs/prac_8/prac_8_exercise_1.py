"""sets={0}
set(sets)
value = 1
bool(value)
while value == 1:
    print("operations on sets")
    print("enter the number in order to perform operations")
    print("0.to add")
    print("1.to remove")
    print("2.to display")
    print("any number to apart from three to end opertaions")
    choice=int(input("enter the value"))
    if(choice == 0):
        n=input("enter the element")
        sets.add(n)
    elif(choice == 1):
        n1=input("enter the element to remove")
        sets.remove(n)
    elif(choice == 2):
        print("the current status:",set(sets))
    else:
        value = 0
print("the final result is :-",set(sets))
set(sets)"""
sets={0,12,30}
set(sets)
sets.add(12)
sets.add(14)
sets.add(15)
sets.remove(15)
print(set(sets))
