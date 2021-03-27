class Node:
    def __init__(self, value, link=None):
        self.value = value 
        self.link = link 

    def get_value(self):
        return self.value 

    def get_link(self):
        return self.link 

    def set_link(self, new_link):
        self.link = new_link

class Stack:
    def __init__(self, top_item=None):
        self.top_item = top_item 
        self.size = 0 
        self.limit = 6

    def is_empty(self):
        if self.size == 0:
            return True 

    def has_space(self):
        if self.limit > self.size:
            return True 

    def push(self, new_value):
        if self.has_space():
            new_node = Node(new_value)
            new_node.set_link(self.top_item)
            self.top_item = new_node 
            self.size += 1
        else:
            print("That row is full")
            pass

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("The row is empty")
    
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item 
            self.top_item = item_to_remove.get_link()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The row is empty")


class Gameplay:
    lane1 = [None for i in range(7)]
    lane2 = [None for i in range(7)]
    lane3 = [None for i in range(7)]
    lane4 = [None for i in range(7)]
    lane5 = [None for i in range(7)]
    lane6 = [None for i in range(7)]
    counter = 5
    winning = []
    checker = 0
    winner_declare = False
    
    
    def gameplay(self):
        print("Welcome to Connect4 !! ")
        
        print('Player 1 will be represented by no. 1 ')
        print('Player 2 will be represented by no. 2')

        board1 = Stack()
        board2 = Stack()
        board3 = Stack()
        board4 = Stack()
        board5 = Stack()
        board6 = Stack()
        board7 = Stack()


        
        
        self.gameboard()
        
        
        print("\n")
        print('This is your gameboard! ')
        print('Here are the controls of your gameboard')
        #Time Sleep 
        print("Each number represents each lane: ")

        playing = True
        self.player_num = 1
        while playing:

            prompt = "Player {num}, please choose a lane: ".format(num=self.player_num)
            
            self.initial_prompt = input(prompt)
            
            if self.initial_prompt == "1":
                board1.push(self.player_num)
                self.first_coin(int(self.initial_prompt) - 1)
                    
                self.winning_functions()

                if self.winner_declare == True:
                    return 
                    break

                else:
                    ## Basic Gameplay
                    if self.lane_empty_checker1(5, 0) == True:
                        self.lane1[0] = str(self.player_num) + " "
                        self.gameboard()
                        print("\n")
                
                    
            
            elif self.initial_prompt == "2":
                board2.push(self.player_num)
                self.first_coin(int(self.initial_prompt) - 1)
                    
                self.winning_functions()

                if self.winner_declare == True:
                    return 
                    break
                    
                else:
                    if self.lane_empty_checker1(5, 1) == True:
                        self.lane1[1] = str(self.player_num) + " "
                        self.gameboard()
                        print("\n")
            
            elif self.initial_prompt == "3":
                board3.push(self.player_num)
                self.first_coin(int(self.initial_prompt) - 1)
                    
                self.winning_functions()

                if self.winner_declare == True:
                    return 
                    break
        
                else:
                    if self.lane_empty_checker1(5, 2) == True:
                        self.lane1[2] = str(self.player_num) + " "
                        self.gameboard()
                        print("\n")
                
            elif self.initial_prompt == '4':
                board4.push(self.player_num)
                self.first_coin(int(self.initial_prompt) - 1)
                    
                self.winning_functions()

                if self.winner_declare == True:
                    return 
                    break
                else:

                    if self.lane_empty_checker1(5, 3) == True:
                        self.lane1[3] = str(self.player_num) + " "
                        self.gameboard()
                        print("\n")
            
            elif self.initial_prompt == '5':
                board5.push(self.player_num)
                self.first_coin(int(self.initial_prompt) - 1)
                    
                self.winning_functions()

                if self.winner_declare == True:
                    return 
                    break
                    
                else:
                    if self.lane_empty_checker1(5, 4) == True:
                        self.lane1[4] = str(self.player_num) + " "
                        self.gameboard()
                        print("\n")

            elif self.initial_prompt == '6':
                board6.push(self.player_num)
                self.first_coin(int(self.initial_prompt) - 1)
                    
                self.winning_functions()

                if self.winner_declare == True:
                    return 
                    break
                else:

                    if self.lane_empty_checker1(5, 5) == True:
                        self.lane1[5] = str(self.player_num) + " "
                        self.gameboard()
                        print("\n")

            elif self.initial_prompt == '7':
                board7.push(self.player_num)
                self.first_coin(int(self.initial_prompt) - 1)
                    
                self.winning_functions()

                if self.winner_declare == True:
                    return 
                    break
                else:
                    if self.lane_empty_checker1(5, 6) == True:
                        self.lane1[6] = str(self.player_num) + " "
                        self.gameboard()
                        print("\n")
            
            if self.player_num == 1:
                self.player_num += 1
            else:
                self.player_num -= 1
    

    def gameboard(self):
        
        self.game_board = [self.lane6, self.lane5, self.lane4, self.lane3, self.lane2, self.lane1]
        for i in self.game_board:
            print("\n")
            print(i)
        row_numbers = [' 1  ', ' 2  ', ' 3  ', ' 4  ', ' 5  ', ' 6  ', ' 7  ']
        for i in row_numbers:
            print(" " + i, end=" ")
    
    def lane_empty_checker1(self, lane, num):
        lanes = {0: self.lane6, 1:self.lane5, 2:self.lane4, 3:self.lane3, 4:self.lane2, 5:self.lane1 }

        if lanes[lane][num] == None:
            return True 
        else:
            return False

    def left_horiziontal_first(self):
        for i in range(len(self.game_board) -1, -1, -1):           ### Function 1 
            neg_one = -1
            neg_two = -2
            neg_three = -3
            neg_four = -4

            if self.game_board[i][neg_one] == str(self.player_num) + " " and self.game_board[i - 1][neg_two] == str(self.player_num) + " " and self.game_board[i - 2][neg_three] == str(self.player_num) + " " and self.game_board[i - 3][neg_four] == str(self.player_num) + " ":
                self.winning_statement()
                return 
                break 
            else:
                continue 

    def left_horizontal_next(self):
        for i in range(len(self.game_board) -1, -1, -1):        ### Function 2
            neg_one = -1 
            neg_two = -2
            neg_three = -3 
            neg_four = -4

            for j in range(5):
                if self.game_board[i][neg_one] == str(self.player_num) + " " and self.game_board[i - 1][neg_two] == str(self.player_num) + " " and self.game_board[i - 2][neg_three] == str(self.player_num) + " " and self.game_board[i - 3][neg_four] == str(self.player_num) + " ":
                    self.winning_statement()
                    return 
                    break 
                else:
                    neg_one -= 1
                    neg_two -= 1
                    neg_three -= 1
                    neg_four -= 1
    
    def right_horizontal_one(self):
        for i in range(len(self.game_board) -1, -1 ,-1):        ### Function 3
            zero = 0
            one = 1
            two = 2
            three = 3 
            
            if i == -1:
                pass
            else:
                if self.game_board[i][0] == str(self.player_num) + " " and self.game_board[i - 1][one] == str(self.player_num) + " " and self.game_board[i - 2][two] == str(self.player_num) + " " and self.game_board[i - 3][three] == str(self.player_num) + " ":
                    self.winning_statement()
                    return
                    break
                else:
                    continue
    
    def right_horizontal_next(self):
        for i in range(len(self.game_board) -1, -1, -1):       ### Function 4
            zero = 0
            one = 1
            two = 2
            three = 3
            for j in range(5):
                

                if self.game_board[i][zero] == str(self.player_num) + " " and self.game_board[i - 1][one] == str(self.player_num) + " " and self.game_board[i - 2][two] == str(self.player_num) + " " and self.game_board[i - 3][three] == str(self.player_num) + " ":
                    self.winning_statement()
                    return
                    break
                else:
                    zero += 1
                    one += 1
                    two += 1
                    three += 1
                    
    def horizontal_one(self):
        for i in self.game_board:                              ### Function 5
            first_four = i[:4]
            second_four = i[1:5]
            third_four = i[2:6]
            fourth_four = i[3:7]

            for j in first_four:
                if j == str(self.player_num) + " ":
                    self.winning.append(j)
                    self.checker += 1
                else:
                    continue 
            if self.checker == 4:
                self.winning_statement()
                return
                break
            self.checker = 0
            self.winning = []

            for j in second_four:
                if j == str(self.player_num) + " ":
                    self.winning.append(j)
                    self.checker += 1
                else:
                    continue 
            if self.checker == 4:
                self.winning_statement()
                return
                break
            self.checker = 0
            self.winning = []

            for j in third_four:
                if j == str(self.player_num) + " ":
                    self.winning.append(j)
                    self.checker += 1
                else:
                    continue 
            if self.checker == 4:
                self.winning_statement()
                return
                break
            
            self.checker = 0
            self.winning = []

            for j in fourth_four:
                if j == str(self.player_num) + " ":
                    self.winning.append(j)
                    self.checker += 1
                else:
                    continue 
            if self.checker == 4:
                self.winning_statement()
                return
                break
            self.checker = 0
            self.winning = []
    
    def horizontal_two(self):
        for i in range(5, -1, -1):                          ### Function 6
            if i == -1:
                pass
            else:
                if self.game_board[i][0] == str(self.player_num) + " ":
                    self.winning.append(self.player_num)
                else:
                    self.winning.append(False)
        first_four = self.winning[:4]
        second_four = self.winning[1:5]
        third_four = self.winning[2:6]

        for i in first_four:                            ### Function 7
            if i == self.player_num:
                self.checker += 1

                if self.checker == 4:
                    self.winning_statement()
                    return
                    break 
            else:
                continue 

        self.checker = 0
        
        for i in second_four:                           ### Function 8
            if i == self.player_num:
                self.checker += 1

                if self.checker == 4:
                    self.winning_statement()
                    return 
                    break
            else:
                continue 
        self.checker = 0

        for i in third_four:                            ### Function 9
            if i == self.player_num:
                self.checker += 1

                if self.checker == 4:
                    self.winning_statement()
                    return
                    break 
            else:
                continue 
        
        if self.winner_declare == False:
            self.winning = []
            self.checker = 0
            self.counter = 5
            self.gameboard()
            print("\n")
        else:
            pass
    
    def winning_functions(self):
        self.left_horiziontal_first()
                    
        self.left_horizontal_next()

        self.right_horizontal_one()

        self.right_horizontal_next()

        self.horizontal_one()
        
        self.horizontal_two()

    def first_coin(self, num):
        if not self.lane_empty_checker1(5, num) == True:
            for i in range(int(len(self.game_board) - 1), -1 , -1):
                if i == -1:
                    pass
                else:
                    if not self.lane_empty_checker1(self.counter, num) == True:
                        self.counter -= 1
                        continue 
                    else:
                        if i == 4:
                            self.lane2[num] = str(self.player_num) + " "
                            break
                        elif i == 3:
                            self.lane3[num] = str(self.player_num) + " "
                            break
                        elif i == 2:
                            self.lane4[num] = str(self.player_num) + " "
                            break
                        elif i == 1:
                            self.lane5[num] = str(self.player_num) + " "
                            break
                        elif i == 0:
                            self.lane6[num] = str(self.player_num) + " "
                            break        
    
    def winning_statement(self):
        self.gameboard()
        print("\n")
        print("Congratulations! player {player} has won! ".format(player=self.player_num))
        self.winner_declare = True

    


test = Gameplay()

test.gameplay()