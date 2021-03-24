import random
import time

money = 100

#Write your game of chance functions here

def intro():
    running = True
    while running:
        print("Hello, would you like to play Heads or Tails, cho-han, pick-cards, Towers of Hanoi, Tic-Tac-Toe, Pokemon, or roulette? ")
        print("Just for the extra info: pick-cards is a 2 player game.")
        time.sleep(1)
        introduction = input("Would game would you like to play?: ")

        if introduction == "Heads or Tails" or introduction == "heads or tails":
            time.sleep(1)
            print(heads_or_tails())
            break
        
        elif introduction == "cho-han" or introduction == "Cho_Han":
            time.sleep(1)
            print(cho_han())
            break

        elif introduction == "pick-cards" or introduction == "Pick-Cards":
            time.sleep(1)
            print(card_flipping())
            break
        elif introduction == "roulette" or introduction == "Roulette":
            time.sleep(1)
            print(roulette())
            break
        
        elif introduction == "Towers of Hanoi" or introduction == "towers of hanoi":
            time.sleep(1)
            from towers_of_hanoi import g
            break

        elif introduction == "Tic Tac Toe" or introduction == "Tic-Tac-Toe":
            time.sleep(1)
            from TicTacToe import test
            break

        elif introduction == "Pokemon" or introduction == "pokemon":
            from pokemon import introduction
            break
        
        else:
            print('That game is currently not valid')



playing = True
def heads_or_tails(): 
    global throw
    global amount
        
    amount = 100
    
    while playing == True:
        num = random.randint(1, 2)
        guess = input("Welcome to Heads or Tails! " + " Please type Heads or Tails to start: ")
        place_wager = int(input("Please enter your wager (any whole number works): "))
        print("You have betted " + str(place_wager) + " dollars!")
        money = 100
        
        
        
         #Heads is thrown and You choose Heads at the start of the game
        if num == 1 and guess == "Heads" or guess == "heads":
            print("Well done! You flipped Heads and you guessed Heads!")
            time.sleep(1)
            amount = amount + place_wager
            print("You have also gained " + str(place_wager) + " dollars. Your total is now " + str(amount) + " dollars!") 
            throw = input("Do you wish to throw again?")
       

        #Heads is thrown and You choose Tails at the start of the game
        if num == 1 and guess == "Tails" or guess == "tails":
            print("Unlucky! You flipped Heads and you guessed Tails!")
            time.sleep(1)
            amount = amount - place_wager
            print("Unfortunately, you lost " + str(place_wager) + " dollars. Your total is now " + str(amount) + " dollars!") 
            throw = input("Do you wish to throw again?")
        
    

        #Tails is thrown and You choose Tails at the start of the game
        if num == 2 and guess == "Tails" or guess == "tails":
            print("Well done! You flipped Tails and you guessed Tails!")
            time.sleep(1)
            amount = place_wager+ amount
            print("You have also gained " + str(place_wager) + " dollars. Your total is now " + str(amount) + " dollars!") 
            throw = input("Do you wish to throw again?")
        

        #Tails is thrown and you choose Heads at the start of the game
        if num == 2 and guess == "Heads" or guess == "heads":
            print("Unlucky! You flipped Tails and you guessed Heads!")
            time.sleep(1)
            amount = amount - place_wager
            print("Unfortunately, you lost " + str(place_wager) + " dollars. Your total is now " + str(amount) + " dollars!") 
            throw = input("Do you wish to throw again?")


        if throw == "yes" or throw == "Yes":
            playing == True
        elif throw == "no" or throw == "No":
            print("Thank you for playing!")
            break
def cho_han():
    global amount 
    global throw

    amount = 100

    while playing == True:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        money = 100
        guess = input("""
        Welcome to Cho-Han! This is a game where you get to guess if the sum of two six-sided di is even or odd. You can also bet some money! You start of with 100 dollars and you lose depending on how much you waged and if you get the guess wrong but also, you gain the amount you waged if you get the guess right! 
        """ + "Please type in Even or Odd to start: ")
        time.sleep(1)
        place_wager = int(input("Please enter your wager (any whole number works): "))
        print("You have betted " + str(place_wager) + " dollars!")
        roll = input("Press *Enter* to roll both dice")
        sum_of_two_dice = dice_1 + dice_2
        
        
        

        #If the sum is even and you choose odd
        if sum_of_two_dice % 2 == 0 and guess == "Even" or guess == "even":
            print("Well done! Your guess is correct!")
            time.sleep(1)
            amount = amount + place_wager
            time.sleep(1)
            print("You have also gained " + str(place_wager) + " dollars. Your total is now " + str(amount) + " dollars!")
            throw = input("Would you like to guess again? ")

     #If the sum is even and you choose odd
        if sum_of_two_dice % 2 == 1 and guess == "Odd" or guess == "odd":
            print("Oops, your guess was wrong. Better luck nex time!")
            time.sleep(1)
            amount = amount - place_wager
            time.sleep(1)
            print("Unfortunately, you lost " + str(place_wager) + " dollars. Your total is now " + str(amount) + " dollars!")
            throw = input("Would you like to guess again? ")
    
        #If the sum is odd and you choose odd
        if sum_of_two_dice % 2 >= 1 and guess == "Odd" or guess == "odd":
            print("Well done! Your guess is correct!")
            time.sleep(1)
            amount = amount + place_wager
            time.sleep(1)
            print("You have also gained " + str(place_wager) + " dollars. Your total is now " + str(amount) + " dollars.")
            throw = input("Would you like to guess again?")
     #If the sum is odd and you choose even
        if sum_of_two_dice % 2 >= 1 and guess == "Even" or guess == "even":
            print("Oops, your guess was wrong. Better luck next time!")
            time.sleep(1)
            amount = amount - place_wager
            time.sleep(1)
            print("Unfortunately, you lost " + str(place_wager) + " dollars. Your total is now " + str(amount) + " dollars!")
            throw = input("Would you like to guess again?")

        if throw == "yes":
            playing == True
        elif throw == "no":
            print("Thank you for playing!")
            break
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





#Call your game of chance functions here

#print(heads_or_tails())
print(intro())
