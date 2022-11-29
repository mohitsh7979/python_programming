# def game(row1,row2,row3):
#     print(row1)
#     print(row2)
#     print(row3)

# row1=[' ',' ',' ']
# row2=[' ',' ',' ']
# row3=[' ',' ',' ']
# row2[1]='x'
# game(row1,row2,row3)


# def choise():
#     choise='WRONG'
#     while choise.isdigit() == False:

#        choise=input("Enter a number : ")

#        if choise.isdigit()== False:
#          print('Sorry that is not digit !')

#     return int(choise)

# print(choise())

# result='Wrong value'

# accept_value=[0,1,2]

# print(result not in accept_value)


# def user_choise():
#     choise='Wrong'
#     acceptable_range=[0,1,2,3,4,5,6,7,8,9]
#     print(acceptable_range)
#     within_range=False
    
#     while choise.isdigit()==False or within_range==False:
#         choise=input('Enter a number in range 0-10 : ')

#         if choise.isdigit()==False:
#             print('Sorry that is not dight !')

#         if choise.isdigit()==True:
#             if int(choise) in acceptable_range:
#                 within_range=True
#             else:
#                 print('Sorry enter number is out of range !')
#                 within_range=False
#     return int(choise)

# print(user_choise())



# game_list=[0,1,2]

# def display_game(game_list):
#     print('Here is the current list')
#     print(game_list)

# display_game(game_list)

# def postion_choise():
#     choise='Wrong'

#     while choise not in ['0','1','2']:
        
#         choise=input('Pick a positon (0,1,2):')

#         if choise not in ['0','1','2']:
#             print('Sorry invalid choise !')
        
#     return int(choise)

# print(postion_choise())


# def replacement_choise(game_list,position):
#     user_placement=input('Type a string to place at postion')
#     game_list[position]=user_placement

#     return game_list

# print(replacement_choise(game_list,1))


# def gameon_choise():
#     choise='Wrong'

#     while choise not in ['Y','N']:
        
#         choise=input('Keep Planing ? (Y or N):')

#         if choise not in ['Y','N']:
#             print('Sorry, I dont Understand ,please choose Y or N')
        
#     if choise == 'Y':
#         return True
#     else:
#         return False

# print(gameon_choise())


# game_on=True
# game_list=[0,1,2]

# while game_on:
#     display_game(game_list)
#     position=postion_choise()
#     game_list=replacement_choise(game_list,position)
#     display_game(game_list)
#     game_on=gameon_choise()

board=[' ']*10

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
    


display_board(board)

# def player_input():
#     marker=''

#     while marker != 'X' and marker !='O':
#         marker=input('Player 1, choose X or O : ')

#     player1=marker

#     if player1 =='X':
#         player2='O'
#     else:
#         player2='X'

#     return (player1,player2)

# print(player_input())