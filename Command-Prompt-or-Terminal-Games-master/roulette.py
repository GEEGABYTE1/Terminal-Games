import random
import time


money = 100


#Write your game functions here

playing = True
def roulette():
    global amount 
    global again

    amount = 100 

    while playing == True:
        spin_gambling = random.randint(1, 3)
        print("Welcome to Roulette or a game sort of like Roulette! ") 
        time.sleep(2)
        print("Extra info: 1 = Red, 2 = Black, 3 = Green")
        time.sleep(2)
        print("Rules: You bet a certain amount of money to see what colour the ball lands on. Red returns the amount you have bet, Black returns double the amount and Green returns triple the amount. It also takes away the same amount if you guess wrong!")
        print("Good Luck!")
        place_wager = int(input("Please enter your wager (any whole number works): "))
        print("You have betted " + str(place_wager) +  " dollars!")
        guess = input("Please type in Red, Black or Green!")
        print("Spinning...")
        time.sleep(1)
        print("Spinning...")
        time.sleep(1)
        print("Spinning...")
        time.sleep(1)
        print("Spinning...")
        time.sleep(1)
        print("Spinning...")
        time.sleep(1)
        print("Spinning...")
        time.sleep(1)
        
        if spin_gambling == 1 and guess == "red" or guess == "Red":
            print("RED")
            print("Well Done! The ball has landed on Red and you have guessed Red!")
            time.sleep(1)
            amount = amount + place_wager 
            print("You have also gained " + str(place_wager) + " dollars since it has laneded on Red and you chose Red. This adds to your total of " + str(amount) + " dollars!")
            again = input("Do you wish to spin again?")

        elif spin_gambling == 1 and guess == "black" or guess == "Black":
            print("RED")
            print("Unlucky, looks like it landed on Red and you chose Black!")
            time.sleep(1)
            amount = amount - place_wager
            print("Because it landed on Red and you guessed Black, " + str(place_wager) + " dollars, will be subtracted from your account making your balance " + str(amount) + " dollars in total.")
            again = input("Do you wish to spin again?")


        elif spin_gambling == 1 and guess == "green" or guess  == "Green":
            print("RED")
            print("Unlucky, looks like it landed on Red and you chose Green!")
            time.sleep(1)
            amount = amount - place_wager
            print("Because it landed on Red and you guessed Green, " + str(place_wager) + " dollars, will be subtracted from your account making your balance " + str(amount) + " dollars in total.")
            again = input("Do you wish to spin again?")

        elif spin_gambling == 2 and guess == "black" or guess == "Black":
            print("BLACK")
            print("Well Done! The ball has landed on Black and you have guessed Black!")
            time.sleep(1)
            amount = amount + (place_wager * 2)
            print("Because it landed on black and you guessed black, you have won double the money you have bet!")
            print("You have gained " + str(place_wager * 2) + " dollars since it has landed on black and you guessed black. This adds to your total of " + str(amount) + " dollars in total!")
            again = input("Do you wish to spin again?")

        elif spin_gambling == 2 and guess == "red" or guess == "Red":
            print("BLACK")
            print("Unlucky, looks like it landed on Black and you chose Red!")
            time.sleep(1)
            amount = amount - (place_wager*2)
            print("Sadly, because it landed on black and you did not guess Black, we will decrease double the amount you have bet.")
            print("Because it landed on black and you guessed Red, " + str(place_wager*2) + "dollars will be subtracted from your account making your balance " + str(amount) + " dollars in total")
            again = input("Do you wish to spin again?")

        elif spin_gambling == 2 and guess == "green" or guess == "Green":
            print("BLACK")
            print("Unlucky, looks like it landed on Black and you chose Green!")
            time.sleep(1)
            amount = amount - (place_wager*2)
            print("Sadly, because it landed on black and you did not guess Black, we will decrease double the amount you have bet.")
            print("Because it landed on black and you guessed Green, " + str(place_wager*2) + " dollars will be subtracted from your account making your balance " + str(amount) + " dollars in total")
            again = input("Do you wish to spin again?")


        elif spin_gambling == 3 and guess == "green" or guess == "Green":
            print("GREEN")
            print("Well Done! The ball has landed on Green and you have guessed Green!")
            time.sleep(1)
            amount = amount + (place_wager * 3)
            print("Because it landed on green and you guessed green, you have won triple the money you have bet!")
            print("You have gained " + str(place_wager * 3) + " dollars since it has landed on green and you have guessed green. This adds to your total of " + str(amount) + " dollars in total")
            again = input("Do you wish to spin again?")

        elif spin_gambling == 3 and guess == "red" or guess == "Red":
            print("GREEN")
            print("Unlucky, looks like it landed on Green and you chose Red!")
            time.sleep(1)
            amount = amount - (place_wager * 3)
            print("Sadly, because it landed on green and you did not guess Green, we will decrease triple the amount you have bet from your balance.")
            print("Because it landed on green and your guess was incorrect, " + str(place_wager*3) + " dollars will be subtracted from your account making your balance " + str(amount) + " dollars in total")
            again = input("Do you wish to spin again?")


        elif spin_gambling == 3 and guess == "black" and guess == "Black":
            print("GREEN")
            print("Unlucky, looks like it landed on Green and you chose Black!")
            time.sleep(1)
            amount = amount - (place_wager * 3)
            print("Sadly, because it landed on green and you did not guess Green, we will decrease triple the amount you have bet from your balance.")
            print("Because it landed on green and your guess was incorrect, " + str(place_wager * 3) + " dollars will be subtracted from your account making your balance " + str(amount) + " dollars in total")
            again = input("Do you wish to spin again?")


        if again == "yes" or again == "Yes":
            playing == True
        elif again == "no" or again == "No":
            print("Thank you for playing!")
            break





#Call your game of chance of functions here

print(roulette())

        