import time
import numpy as np
import sys
import site

# Delay printing

def delay_print(s):

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create the class
class Pokemon:
    def __init__(self, name, types, moves, EVs, revives=2, xp=5, potion=2, health='==================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars
        self.revives = revives
        self.xp = xp
        self.potion = potion
        

    def fight(self, Pokemon2):
        # Allow two pokemon to fight each other

        # Print fight information
        print("-----POKEMONE BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(2)

        # Consider type advantages
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                # Both are same type
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # Pokemon2 is STRONG
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Pokemon2 is WEAK
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'


        # Now for the actual fighting...
        # Continue while pokemon still have health
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print("*You have " + str(self.potion) + " health potions left*")
            time.sleep(0.5)
            heal = input("\nUse a health potion (please type yes or no): ")
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""
            self.xp += 5

            if self.xp == 15:
                print(test1())


            #Using the potion 
            if self.bars < 20:
                if self.potion != 0:
                    if heal == "yes":
                        print("\n")
                        delay_print("You have used a potion!")
                        for i in range(5):
                            self.bars += 1
                            self.health += "=" * 1
                            if self.bars == 20:
                                break
                        self.potion -=1 
            if self.bars == 20:
                if heal == "yes":
                    print("\n")
                    delay_print("You cannot use the potion as your pokemon is already max health!")
                    
            if self.bars < 20:
                if self.potion == 0:
                    if heal == "yes":
                        print("\n")
                        delay_print("You cannot heal your pokemon as you do not have any more potions left!")
                        
                        

            # Add back bars plus defense boost
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')
                time.sleep(2)
                print()
                revive = input("Player 2, would you like to revive your pokemon?")
                if revive == "yes" or revive == "Yes":
                    if Pokemon2.revives > 0:
                        Pokemon2.bars = 20
                        Pokemon2.health += "=" * 20
                        print("{} has been revived!".format(Pokemon2.name))
                        Pokemon2.revives -= 1

                    if Pokemon2.revives == 0:
                        print("You do not have any revives left!")
                        question = input('Would you like to play again?')
                        if question == "no" or "No":
                            Pokemon2.bars = 0
                            money = np.random.choice(5000)
                            delay_print(f"\nPlayer2 pays Player1  ${money}.\n")
                            exit()
                        if question == "yes" or question == "Yes":
                            print(introduction())

                if revive == "no" or revive =="No":
                    question = input("Would you like to play again?")
                    if question == "no" or question == "No":
                        money = np.random.choice(5000)
                        delay_print(f"\nPlayer2 pays Player1 ${money}.\n")
                        exit()
                    if question == "yes" or question == "Yes":
                        print(introduction())    
                
            # Pokemon2s turn

            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print("*You have " + str(self.potion) + " health potions left*")
            time.sleep(0.5)
            heal = input("\nUse a health potion (please type yes or no): ")
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            self.bars -= Pokemon2.attack
            self.health = ""
            Pokemon2.xp += 5

             #Using the potion 
            if Pokemon2.bars < 20:
                if Pokemon2.potion != 0:
                    if heal == "yes":
                        print("\n")
                        delay_print("You have used a potion!")
                        for i in range(5):
                            Pokemon2.bars += 1
                            Pokemon2.health += "=" 
                            if Pokemon2.bars == 20:
                                break
                        Pokemon2.potion -=1 
            if self.bars == 20:
                if heal == "yes":
                    print("\n")
                    delay_print("You cannot use the potion as your pokemon is already max health!")
                    
            if self.bars < 20:
                if self.potion == 0:
                    if heal == "yes":
                        print("\n")
                        delay_print("You cannot heal your pokemon as you do not have any more potions left!")
                        


            # Add back bars plus defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                time.sleep(2)
                print()
                revive = input("Player 1, would you like to revive your pokemon?")
                if revive == "yes" or revive == "Yes":
                    if self.revives > 0:
                        self.bars = 20
                        self.health += "=" * 20
                        print("{} has been revived!".format(self.name))
                        self.revives -= 1

               
                    if self.revives == 0:
                        print("You do not have any revives left, sadly your pokemon has died!")
                        question == input("Would you like to play again?")
                        if question == "no" or question =="No":
                            money = np.random.choice(5000)
                            delay_print(f"\nPlayer1 pays Player2 ${money}.\n")
                            exit()
                        if question == "yes" or question == "Yes":
                            print(introduction())
                        
                if revive == "no" or revive =="No":
                    question = input("Would you like to play again?")
                    if question == "no" or question == "No":
                        Pokemon2.bars = 0
                        money = np.random.choice(5000)
                        delay_print(f"\nPlayer1 pays Player2 ${money}.\n")
                        exit()
                    if question == "yes" or question == "Yes":
                        print(introduction())
            
       

            





if __name__ == '__main__':
    #Create Pokemon
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'], {'ATTACK': 10, 'DEFENSE':10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'], {'ATTACK':4, 'DEFENSE':2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],  {'ATTACK': 3, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'], {'ATTACK':2, 'DEFENSE':4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'], {'ATTACK':6, 'DEFENSE':5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'], {'ATTACK': 5, 'DEFENSE':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6})


def introduction():
    print("Welcome to Pokemon Battles.")
    print("Player 1, please choose your pokemon!")
    player1 = int(input("""
    You have 3 pokemon to choose from!
    1. Charmander
    2. Squirtle
    3. Bulbasaur
    4. Charmeleon 
    5. Wartortle 
    6. Ivysaur
    7. Charizard 
    8. Blastoise 
    9. Venusaur
    Please type a number to choose your pokemon
    """))
    print("Player 2, please choose your pokemon!")
    player2 = int(input("""
    You have 3 pokemon to choose from!
    1. Charmander
    2. Squirtle
    3. Bulbasaur
    4. Charmeleon 
    5. Wartortle 
    6. Ivysaur
    7. Charizard 
    8. Blastoise 
    9. Venusaur
    Please type a number to choose your pokemon
    """))

    choices = {1: Charmander, 2: Squirtle, 3:Bulbasaur, 4: Charmeleon, 5:Wartortle, 6:Ivysaur, 7: Charizard, 8: Blastoise, 9:Venusaur}

    choices[player1].fight(choices[player2])

    #Charizard.fight(Blastoise) # Get them to fight

            

print(introduction())


        