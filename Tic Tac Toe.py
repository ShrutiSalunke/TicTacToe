#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


# In[2]:


row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']


# In[3]:


display(row1,row2,row3)


# In[4]:


def user_choice():
    
    choice = "WRONG"
    acceptable_range = range(0,10)
    within_range = False 
    while choice.isdigit()== False or within_range== False:
        choice = input("Enter a number between 0-9: ")
        
        
        if choice.isdigit() == False:
            print("SOrry wrong input")
            
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry you are out of acceptable range!")
                within_range = False
    return int(choice)


# In[5]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])


# In[6]:


test_board= ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[7]:


def player_input():
    
    marker = ''
    
    while marker != 'X' and marker!= 'O':
        marker = input("Player 1: Please Choose 'X' or 'O'").upper()
    
    if marker == "X":
        return ('X','O')
    else:
        return ('O','X')


# In[8]:


def place_marker(board,marker,position):
    board[position] = marker


# In[9]:


def win_check(board,mark):
    #rows
    return ((board[1] == mark and board[2] == mark and board[3] == mark ) or
    (board[4] == mark and board[5] == mark and board[6] == mark ) or
    (board[7] == mark and board[8] == mark and board[9] == mark ) or
    #columns
    (board[1] == mark and board[4] == mark and board[7] == mark ) or
    (board[2] == mark and board[5] == mark and board[8] == mark ) or
    (board[3] == mark and board[6] == mark and board[9] == mark ) or
    # diagonals
    (board[1] == mark and board[5] == mark and board[9] == mark ) or
    (board[3] == mark and board[5] == mark and board[7] == mark ))


# In[10]:


import random

def choose_first():
    flip = random.randint(0,1)
    
    if flip == '0':
        return ' Player 1 '
    else:
        return 'Player 2'


# In[11]:


def space_check(board,position):
    return board[position] == ' '


# In[12]:


def full_board_check(board):
    for i in range(0,10):
        if space_check(board,i):
            return False
    return True


# In[13]:


def player_choice(board):
    position = 0 
    while position not in range(0,10) or not space_check(board,position):
        position = int(input("Please enter a position from 0 to 9 : "))
    return position


# In[14]:


def replay():
    choice = input("Play again? Enter Yes or No")
    return choice == 'Yes'


# In[15]:


print("Welcome to TIC TAC TOE!")

while True:
    the_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker ,player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first")
    play_game = input("Ready? y or n")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on :
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 has won!!!")
                game_on = False
                
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Player 2 has won!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    
                    
                    
                    
                    
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break


# In[ ]:





# In[ ]:





# In[ ]:




