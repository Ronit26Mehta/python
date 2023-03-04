import calendar
yy=2023
mm=int(input("enter the month of the year 2023:-"))
if(mm<=12):
    print("the calender is \r",calendar.month(yy,mm))
else:
    print("there are only 12 months")
