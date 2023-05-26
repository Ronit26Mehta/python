value = True
while value == True:
    age = int(input("enter the age"))
    try:
        if(age<18):
            raise Exception
        else:
            print("eligible for voting")
            value = False
    except Exception:
        print("not elligible for voting")
    finally:
        print("operations done successfully")