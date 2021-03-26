import random 
import time 

money = 100 

#Write your game functions here
playing = True
def card_flipping():
    global amount 
    global flip 

    amount = 100 
    amount2 = 100 


    J = 11 
    Q = 12
    K = 13 

    while playing == True:
        card_one = random.randint(1, 13)
        card_two = random.randint(1, 13)
        intro = input("Welcome to Card Flip! " + " Please click *enter* to continue")
        time.sleep(1)
        print(" This game is all about luck!")
        time.sleep(1)
        print("Extra info : Ace = 1, Jack = 11 , Q = 12, K = 13")
        guess = input("Player 1, please choose any card from the deck by pressing *enter*: ")
        place_wager = int(input("Player 1, please enter your wager (any whole number works): "))
        print("Player 1 has betted " + str(place_wager) + " dollars!")
        guess2 = input("Player 2, please choose any card from the deck by pressing *enter*: ")
        place_wager2 = int(input("Player 2, please enter your wager (any whole number works): "))
        print("Player 2 has betted " + str(place_wager2) + " dollars!")


    #If player One chooses a higher number than player 2
        if card_one > card_two:
            print("Alright, let's see what you guys have chosen...")
            time.sleep(1)
            print("Player 1 has chosen " + str(card_one))
            time.sleep(1)
            print("Player 2 has chosen " + str(card_two))
            time.sleep(2)
            print("Well done Player 1! You have won the bet. ")
            time.sleep(1)
            amount = amount + place_wager + place_wager2 
            amount2 = amount2 - place_wager2 
            print("Congratulations player 1, you have won your bet but also, you have gained money from player 2's bet. " + "Your total earnings are " + str(place_wager + place_wager2) + " dollars, which adds to your total of " + str(amount))
            time.sleep(2)
            print("Sadly player 2 has lost this bet and lost " + str(place_wager2) + " dollars, which decreases his/her total of " + str(amount2))
            flip = input("Would you guys like to flip again?")

        if card_one < card_two:
            print("Alright, let's see what you guys have chosen...")
            time.sleep(1)
            print("Player 1 has chosen " + str(card_one))
            time.sleep(1)
            print("Player 2 has chosen " + str(card_two))
            time.sleep(2)
            print("Well done player 2! You have won the bet. ")
            amount = amount - place_wager
            amount2 = amount2 + place_wager + place_wager2
            print("Congratulations player 2, you have won your bet but also, you have gained money from player 1's bet. " + "Your total earnings are " + str(place_wager2 + place_wager) + " dollars, which adds to your total of " + str(amount2))
            time.sleep(2)
            print("Sadly player 1 has lost this bet and lost " + str(place_wager) + " dollars, which decreases his/her total of " + str(amount))
            flip = input("Would you guys like to flip again?")

        if card_one == card_two:
            print("WOW, looks like you guys choose the same card!")
            time.sleep(1)
            print("There will be no affect on any of your balances!")
            flip = input("Would you guys like to flip again?")
            

        if flip == "yes" or flip == "Yes":
            playing == True
        elif flip == "no" or flip == "No":
            print("Thank you for playing!")
            break


#Call your game of chance of functions here
print(card_flipping())