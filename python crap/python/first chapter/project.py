import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90))#Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter3=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter4=chr(random.randint(65,90))#Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter5=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter6=chr(random.randint(65,90))#Generate a random Uppercase letter (based on ASCII code)
#Generate more characters here
#....

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 +uppercaseLetter5 + uppercaseLetter6 # + ....
password = shuffle(password)

#Ouput
print("group no.24 microproject random password generator")
print("the password is here=",password)
