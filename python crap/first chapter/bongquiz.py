print("welcome to the quiz")
print("the question for you is ")
print("napolean was defeated for the last time in his life")
print("1.waterloo")
print("2.bulge")
print("3.warsaw")
print("4.moscow")
answer={1:"waterloo",2:"bulge",3:"warsaw",4:"moscow"}
n=int(input("enter the correct number"))
if(answer[n]==1):
      print("you nailed it")
else:
    print(answer[n],"napolean never lost there")
    
