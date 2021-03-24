import random 
import time 


money = 100

#Write your game functions here 

playing = True
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


        















#Call your game functions here
print(cho_han())