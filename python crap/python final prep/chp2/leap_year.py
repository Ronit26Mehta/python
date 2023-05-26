year = int(input("enter the year:"))
if(year%4 == 0 ):
    print("the {} is leap year".format(year))
else:
    print("the {} is not a leap year".format(year))