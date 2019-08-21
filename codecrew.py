### Problem 1:
#Create two variables. One should equal “My name is: “ and the other should equal your actual name. Print the two variables in one print message.
sentence = "My name is: "
username = "marcus"
print(sentence + username)


#Ask the user to enter the extra credit they earned. If they entered less than 5 print “That’s not enough extra credit.” If they entered more than 20 print “That’s too much extra credit”.

userCredit = int(input("enter extra credit "))

if userCredit < 5:
   print("that's not enough extra credit")
elif userCredit > 20:
   print("that too much extra credit")

### Problem 3:
#Ask a user to enter a password. Enter a password. Ask user to reenter password. Check to see if they are correct.

userInput = input("enter a password ")
userInput2 = input("reenter password ")
if userInput == userInput2:
   print("correct")
else:
   print("incorrect")


## Problem 4:
#Ask for two card numbers. If it equals 21 print BLACKJACK!, if it’s greater than 21 print BUST!, if it’s less than 21 print “The total is [THE TOTAL]”
card1 = int(input("enter a card number"))
card2 = int(input("enter a card number"))
sum = card1 + card2
if sum == 21:
    print("BLACKJACK!")
elif sum > 21:
    print("BUST!")
elif sum < 21:
    print("the total is: " + str(sum))