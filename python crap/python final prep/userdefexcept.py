class password_not_found_exception(Exception):
    pass
value = True
while value == True:
    try :
       password = str(input("enter password"))
       if (password != "ron123"):
           raise password_not_found_exception
       else:
           print("log in complete")
           value = False
    except password_not_found_exception:
        print("not a valid password try again")
    finally:
        print("operations done")