import time

class gameplay:
    def __init__(self, top, middle, bottom):
        self.top = top
        self.middle = middle
        self.bottom = bottom 
    
        
    
    def display_board(self):
        print(self.top)
        print(self.middle)
        print(self.bottom)

    def top_left(self, mark):                                   ####################### Top Lane ############################
        self.mark = mark
        letter = []
        letter.append(self.mark)
        self.total = letter + self.top[1:]
        self.top = self.total 
        
    
    def top_mid(self, mark):
        self.mark = mark
        letter = []
        letter.append(self.mark)
        part_one = self.top[:1]
        part_two = self.top[-1:]
        self.total2 = part_one + letter + part_two 
        self.top = self.total2
        
    
    def top_right(self, mark):
        self.mark = mark
        letter = []
        letter.append(self.mark)
        self.total3 = self.top[:-1] + letter
        self.top = self.total3
        
    
    def mid_left(self, mark):                                       ###################### Middle Lane ###########################
        self.mark = mark
        letter = []
        letter.append(self.mark)
        self.total4 = letter + self.middle[1:]
        self.middle = self.total4
        
    
    def mid_mid(self, mark):
        self.mark = mark
        letter = []
        letter.append(self.mark)
        part_one = self.middle[:1]
        part_two = self.middle[-1:]
        self.total5 = part_one + letter + part_two 
        self.middle = self.total5
        
    
    def mid_right(self, mark):
        self.mark = mark
        letter = []
        letter.append(self.mark)
        self.total6 = self.middle[:-1] + letter
        self.middle = self.total6 
        
    
    def bottom_left(self, mark):                                ##################### Bottom Lane ###########################
        self.mark = mark
        letter = []
        letter.append(self.mark)
        self.total7 = letter + self.middle[1:]
        self.bottom = self.total7
        #return board.display_board()
    
    def bottom_mid(self, mark):
        self.mark = mark
        letter = []
        letter.append(self.mark)
        part_one = self.bottom[:1]
        part_two = self.bottom[-1:]
        self.total8 = part_one + letter + part_two 
        self.bottom = self.total8
        
    
    def bottom_right(self, mark):
        self.mark = mark 
        letter = []
        letter.append(self.mark)
        self.total9 = self.bottom[:-1] + letter
        self.bottom = self.total9
        
    

        
            


#print(board.display_board())
#print(board.bottom_right("X"))


class introduction:
    def __init__(self):
        print('Hello there! Welcome to tic-tac-toe!')
        time.sleep(1)
        initialize = str(input('Would you like to play? (Please enter \'Y\' for Yes and \'N\' for No) '))
        if initialize == "Y":
            board = gameplay(['*', '*', '*'], ['*', '*', '*'], ['*','*','*'])
            print(board.display_board())
            

            player1 = str(input("Player1, please choose your mark (ex, X or O): "))
            time.sleep(1)
            player2 = str(input("Player2, please choose your mark (ex, X or O): "))

            if player1 == player2:
                print("Oops, looks like you guys chose the same mark, please choose again: ")
                player1 = str(input("Player1, please choose your mark (ex, X or O): "))
                time.sleep(1)
                player2 = str(input("Player2, please choose your mark (ex, X or O): "))
            
            time.sleep(1)

            print(board.display_board())

            options = [
                "Top Left", "Top Middle", "Top Right",
                "Middle Left", "Middle", "Middle Right"
                "Bottom Left", "Bottom Middle", "Bottom Right"
            ]
            
            print("Here are your options on the board. ") 
            time.sleep(0.5)
            print(options)    
            time.sleep(1)
            print("Let's get playing!!!")
            playing = True 
            while playing:

                if player1 == board.top[0] and player1 == board.middle[1] and player1 == board.bottom[-1]:
                    print("Congratulations Player1, you have won the game! ")
                    break 
                elif player1 == board.top[-1] and player1 == board.middle[1] and player1 == board.bottom[0]:
                    print("Congratulations Player1, you have won the game! ")
                    break
                
                elif player1 == board.bottom[0] and player1 == board.bottom[1] and player1 == board.bottom[-1]:
                    print("Congratulations Player1, you have won the game! ")
                    break
                
                elif player1 == board.middle[0] and player1 == board.middle[1] and player1 == board.bottom[-1]:
                    print("Congratulations Player1, you have won the game! ")
                    break 
                
                elif player1 == board.top[0] and player1 == board.top[1] and player1 == board.top[-1]:
                    print("Congratulations Player1, you have won the game! ")
                    break
                
                elif player1 == board.top[0] and player1 == board.bottom[0] and player1 == board.middle[0]:
                    print("Congratulations Player1, you have won the game! ")
                    break
                
                elif player1 == board.top[1] and player1 == board.middle[1] and player1 == board.bottom[1]:
                    print("Congratulations Player1, you have won the game! ")
                    break 

                elif player1 == board.top[-1] and player1 == board.middle[-1] and player1 == board.bottom[-1]:
                    print("Congratulations Player1, you have won the game! ")
                    break 
                
                elif player2 == board.top[0] and player2 == board.middle[1] and player2 == board.bottom[-1]:
                    print("Congratulations Player2, you have won the game! ")
                    break 
                elif player2 == board.top[-1] and player2 == board.middle[1] and player2 == board.bottom[0]:
                    print("Congratulations Player2, you have won the game! ")
                    break
                
                elif player2 == board.bottom[0] and player2 == board.bottom[1] and player2 == board.bottom[-1]:
                    print("Congratulations Player2, you have won the game! ")
                    break
                
                elif player2 == board.middle[0] and player2 == board.middle[1] and player2 == board.bottom[-1]:
                    print("Congratulations Player2, you have won the game! ")
                    break 
                
                elif player2 == board.top[0] and player2 == board.top[1] and player2 == board.top[-1]:
                    print("Congratulations Player2, you have won the game! ")
                    break
                
                elif player2 == board.top[0] and player2 == board.bottom[0] and player2 == board.middle[0]:
                    print("Congratulations Player2, you have won the game! ")
                    break
                
                elif player2 == board.top[1] and player2 == board.middle[1] and player2 == board.bottom[1]:
                    print("Congratulations Player2, you have won the game! ")
                    break 

                elif player1 == board.top[-1] and player1 == board.middle[-1] and player1 == board.bottom[-1]:
                    print("Congratulations Player2, you have won the game! ")
                    break 
                
                elif not '*' in board.top and not '*' in board.middle and not '*' in board.bottom:
                    print("It's a tie!")
                    break
                
                else:
                    

                    question1 = str(input("Player1, where would you like to put your mark? "))
                    
                                                                                ##### Player1 Prompt #####
                    if question1 == "Top Left" or question1 == "top left":
                        if board.top[0] == '*':
                            board.top_left(player1)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question1)
                        
                    elif question1 == "Top Middle" or question1 == "top middle":
                        if board.top[1] == '*':
                            board.top_mid(player1)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question1)

                    elif question1 == "Top Right" or question1 == "top right":
                        if board.top[-1] == '*':
                            board.top_right(player1)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question1)
                        
                    elif question1 == "Middle Left" or question1 == "middle left":
                        if board.middle[0] == '*':
                            board.mid_left(player1)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question1)
                        
                    elif question1 == "Middle" or question1 == "middle":
                        if board.middle[1] == '*':
                            board.mid_mid(player1)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question1)
                        
                    elif question1 == "Middle Right" or question1 == "middle right":
                        if board.middle[-1] == '*':
                            board.mid_right(player1)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question1)
                        
                    elif question1 == "Bottom Left" or question1 == "bottom left":
                        if board.bottom[0] == '*':
                            board.bottom_left(player1)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question1)
                        
                    elif question1 == "Bottom Middle" or question1 == "bottom_middle":
                        if board.bottom[1] == '*':
                            board.bottom_mid(player1)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question1)
                        
                    elif question1 == "Bottom Right" or question1 == "bottom right":
                        if board.bottom[-1] == '*':
                            board.bottom_right(player1)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question1)
                        
                    else:
                        print("Oops looks like you did not choose the correct option!")
                        prompt1 = str(input("Would you like to choose again? "))
                        if prompt1 == "yes" or "Yes":
                            print(question1)
                        else:
                            print("You have skipped your turn")

                    options1 = ["Top Left", "top left", "Top Middle", "top middle", "Top Right", "top right", "Middle Left", "middle left", "Middle", "middle", "Middle Right", "middle right", "Bottom Left", "bottom left", "Bottom Middle", "bottom middle", "Bottom Right", "bottom right" ]

                    question2 = str(input("Player2, where would you like to put your mark? "))
                    
                                                                                ##### Player2 prompt #######
                    if question2 == "Top Left" or question2 == "top left":
                        if board.top[0] == '*':
                            board.top_left(player2)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question2)
                        
                    elif question2 == "Top Middle" or question2 == "top middle":
                        if board.top[1] == '*':
                            board.top_mid(player2)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question2)
                        
                    elif question2 == "Top Right" or question2 == "top right":
                        if board.top[-1] == '*':
                            board.top_right(player2)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question2)
                        
                    elif question2 == "Middle Left" or question2 == "middle left":
                        if board.middle[0] == '*':
                            board.mid_left(player2)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question2)
                        
                    elif question2 == "Middle" or question2 == "middle":
                        if board.middle[1] == '*':
                            board.mid_mid(player2)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question2)
                        
                    elif question2 == "Middle Right" or question2 == "middle right":
                        if board.middle[-1] == '*':
                            board.mid_right(player2)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question2)
                        
                    elif question2 == "Bottom Left" or question2 == "bottom left":
                        if board.bottom[0] == '*':
                            board.bottom_left(player2)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question2)
                        
                    elif question2 == "Bottom Middle" or question2 == "bottom_middle":
                        if board.bottom[1] == '*':
                            board.bottom_mid(player2)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question2)
                        
                    elif question2 == "Bottom Right" or question2 == "bottom right":
                        if board.bottom[-1] == '*':
                            board.bottom_right(player2)
                            print(board.display_board())
                        else:
                            print("Oops, looks like someone has already chosen that spot!")
                            print(question2)
                        
                    else:
                        print("Oops looks like you did not choose the correct option!")
                        prompt2 = str(input("Would you like to choose again?"))
                        if prompt2 == "yes" or "Yes":
                            print(question2)
                        else:
                            print("You have skipped your turn")
                        

                



            else:
                return "Goodbye"




test = introduction()
print(test)




