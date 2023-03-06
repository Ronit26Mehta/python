while True:
    n=int(input("enter the password"))
    try:
        password1=1234
        
        if n!=password1:
            raise Exception
        else:
            print("the password was correct")
            break
    except Exception:
        print("try again")
