
from IPython.display import clear_output
board=[]
def display_board(board):

   
    print('-------------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('-------------')


# function take input X or O from player 

def take_input():
    marker=''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1:Do you want to be X or O?')
        
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    




def place_marker(board, marker, position):
    board[position] = marker


# Function to check if any player won 

def win_check(board,mark):
    
    return (board[1]==mark and board[2]==mark and board[3]==mark)or(board[4]==mark and board[5]==mark and board[6]==mark) or(board[7]==mark and board[8]==mark and board[9]==mark) or(board[1]==mark and board[4]==mark and board[7]==mark) or(board[2]==mark and board[5]==mark and board[8]==mark) or(board[3]==mark and board[6]==mark and board[9]==mark) or(board[1]==mark and board[5]==mark and board[9]==mark) or(board[3]==mark and board[5]==mark and board[7]==mark)
            
        


# function to start from any random player

import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player_1'
    else:
        return 'Player_2'




def space_check(board,position):
    return board[position] == ' '




def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True





def take_position(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Enter the position from 1 - 9'))
        
    return position


# In[11]:


def replay():
    play = input("Do you want to play again ? Type 'Yes' or 'No' ")
    if play.lower().startswith('y'):
        return True
    else:
        return False





print('********WELCOME TO THE TIC TAC TOE GAME********')

while True:
    theboard = [' ']*10
    player1_marker,player2_marker = take_input()
    turn = choose_first()
    print(turn + 'will go first')
    play = input('ARE YOU READY TO PLAY ? PRESS Yes or No')
    
    if play[0].lower() == 'y':
        game = True
    else:
        game = False
        
    while game:
        if turn == 'Player_1':
            position1 = take_position(theboard)
            place_marker(theboard,player1_marker,position1)
            display_board(theboard)
        
            if win_check(theboard,player1_marker):
                display_board(theboard)
                print('Congratulations....!!!! Player 1 won the match ')
                game = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('MATCH IS DRAW')
                    break
                else:
                    turn = 'Player_2'
                    
        else:
            position2 = take_position(theboard)
            place_marker(theboard,player2_marker,position2)
            display_board(theboard)
            
            if win_check(theboard,player2_marker):
                display_board(theboard)
                print('Congratulations.......!!!!!Player 2 won the match ' )
                game = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('MATCH IS DRAW')
                    break
                else:
                    turn = 'Player_1'
                    
            
    if not replay():
        break
                
            


# Combination of all the functions 

# In[ ]:



        
            
            
            
        
            
            


    

