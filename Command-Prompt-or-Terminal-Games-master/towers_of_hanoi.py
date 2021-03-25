import time
import site


class node:
    def __init__(self, data=None):
        self.data = data 
        self. next = None

    def get_value(self):
        return self.data 

    def get_link(self):
        return self.next 


    def set_link(self, new_link):
        self.next = new_link


print("\nHello there welcome to towers of Hanoi!")
num_disks = int(input("How many disks would you like to play with: "))

class Stack():
    global num_disks
    def __init__(self, limit=1000):
        self.top_item = None
        self.limit = limit 
        self.size = 0 

    def has_space(self):
        return self.size != num_disks

    def is_empty(self):
        return self.size == 0 

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            return 0

    def push(self, new_data):
        if self.has_space():
            new_node = node(new_data)
            new_node.set_link(self.top_item)
            self.top_item = new_node
            self.size += 1
        else:
            return 'The stack is full'

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item 
            self.top_item = item_to_remove.get_link()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            return "There is nothing to take out"



top_stack = Stack()
middle_stack = Stack()
bottom_stack = Stack()
lst1 = []
lst2 = []
lst3 = []
class game(Stack):

    for i in range(num_disks, 0, -1): 
        top_stack.push(i)
        lst1.append(i)


    print(lst1)
    print(lst2)
    print(lst3)
    print("\nThis is your game board")            
    time.sleep(0.5)

    print("You have three choices to put your disks in: ")
    choices = ["Top", "Middle", "Bottom"]
    for i in choices:
        print("\n" + i)
    user_moves = 0
    playing = True
    while playing:
        #This is if he decides to use the top lane to move the disks 
        print("\n")
        option = str(input("Which lane would you like to work with?: "))
        
        if option == "/quit":
            break
        
        if option == "Top" or option == "top":
            throw = str(input("Where would you like to put your disk?: "))
            if throw == "Middle" or throw == "middle":
                if middle_stack.has_space():
                    if top_stack.peek() < middle_stack.peek() or middle_stack.peek() == 0:
                        middle_stack.push(top_stack.peek())
                        top_stack.pop()
                        user_moves += 1
                        #Showing how the disks look 
                        lst2.append(lst1[-1])
                        lst1 = lst1[:-1]
                        print(lst1)
                        print(lst2)
                        print(lst3)
                        print("Moves:" + str(user_moves))
                        
                        
                    else:
                        print("Sadly, you cannot move there as there is already a bigger disk there")
                        


            if throw == "Bottom" or throw == "bottom":
                if bottom_stack.has_space():
                    if top_stack.peek() < bottom_stack.peek() or bottom_stack.peek() == 0:
                        bottom_stack.push(top_stack.peek())
                        top_stack.pop()
                        user_moves += 1

                        #Showing how the disks look 
                        lst3.append(lst1[-1])
                        lst1 = lst1[:-1]
                        print(lst1) 
                        print(lst2)
                        print(lst3)  
                        print("Moves:" + str(user_moves))
                        
                    else:
                        print("Sadly, you cannot move there as there is already a bigger disk there")
                        option = str(input("Which lane would you like to work with?: "))

            if throw == "Top" or throw == "top":
                print("Your disk is already there ")
                

        #This if he decides to use the middle lane to move the disks
        
        if option == "Middle" or option == "middle":
            throw = str(input("Where would you like to put your disk?: "))
            if throw == "Bottom" or throw == "bottom":
                if bottom_stack.has_space():
                    if middle_stack.peek() < bottom_stack.peek() or bottom_stack.peek() == 0:
                        bottom_stack.push(middle_stack.peek())
                        middle_stack.pop()
                        user_moves += 1
                        #Showing how the disks look 
                        lst3.append(lst2[-1])
                        lst2 = lst2[:-1]
                        print(lst1)
                        print(lst2)
                        print(lst3)
                        print("Moves:" + str(user_moves))
                    else:
                        print("Sadly, you cannot move there as there is already a bigger disk there")
                        
            
            if throw == "Top" or throw == "top":
                if top_stack.has_space():
                    if middle_stack.peek() < top_stack.peek() or top_stack.peek() == 0:
                        top_stack.push(middle_stack.peek())
                        middle_stack.pop()
                        user_moves += 1
                        #Showing how the disks look
                        lst1.append(lst2[-1])
                        lst2 = lst2[:-1]
                        print(lst1)
                        print(lst2)
                        print(lst3)
                        print("Moves:" + str(user_moves))
                        
                    
                    else:
                        print("Sadly, you cannot move there as there is already a bigger disk there")
                        


            if throw == "Middle" or throw == "middle":
                    print('Your disk is already there!')
                    


            #This if user decides to use the bottom lane to move the disls 
        
        if option == "bottom" or option == "Bottom":
            throw = str(input("Where would you like to put your disk?: "))
            if throw == "Top" or throw == "top":
                if top_stack.has_space():
                    if bottom_stack.peek() < top_stack.peek() or top_stack.peek() == 0:
                        top_stack.push(bottom_stack.peek())
                        bottom_stack.pop()
                        user_moves += 1

                        #Showing how the disks look 
                        lst1.append(lst3[-1])
                        lst3 = lst3[:-1]
                        print(lst1) 
                        print(lst2)
                        print(lst3)
                        print("Moves:" + str(user_moves))
                        
                    else:
                        print("Sadly, you cannot move there as there is already a bigger disk there")
                        

            if throw == "Middle" or throw == "middle":
                if middle_stack.has_space():
                    if bottom_stack.peek() < middle_stack.peek() or middle_stack.peek() == 0:
                        middle_stack.push(bottom_stack.peek())
                        bottom_stack.pop()
                        user_moves += 1

                        #Showing how the disks work
                        lst2.append(lst3[-1])
                        lst3 = lst3[:-1]
                        print(lst1)
                        print(lst2)
                        print(lst3)
                        print("Moves:" + str(user_moves))
                        
                        
                    else:                  
                        print("Sadly, you cannot move there as there is already a bigger disk there")
                        

            if throw == "Bottom" or throw == "bottom":
                print("Your disk is already there!")
                


        #If user wins
        winning_lst = []
        for i in range(num_disks):
            winning_lst.append(i)
        
        if lst3 == winning_lst:
            print("Congratulations, you have won the game!")
            exit()
            


                    
                    
                    
                    
                    
                







g = game()


        
