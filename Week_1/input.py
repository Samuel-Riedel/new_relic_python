askName = input("what is your name? ")
askAge = int(input("What is your age? "))
askCountry = input("Where are you from? ")
askHeight = float(input("What is your height "))

askBarcelona = input("Are you a fan of Barcelona? ").lower()
booleanAnswer = askBarcelona =="yes"

print("My name is: " + askName + " my age is: " + str(askAge) + " I was born in: " + askCountry + " my height is: " + str(askHeight ) + 
" is he a fan of Barcelona? " + str(booleanAnswer))




### Old Code Lines ##

#askName = print ("Hello " + input("what is your name?"))
#askAge = print("Your age is : " + input("What is your age?"))
#askCountry = print("You are from: " + input(" Where are you from? "))
#askHeight = print("Your height is: " + input("What is your height"))

#askName = print ("Hello " + input("what is your name?"))
#askAge = input("What is your age?")
#print(int(askAge))
#askCountry = print("You are from: " + input(" Where are you from? "))
#askHeight = input("What is your height ")
#print(float(askHeight))