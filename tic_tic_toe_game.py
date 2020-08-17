#to dispaly tic toc toe board after each turn
def viewDashboard():
    os.system('clear')
    print("\n")
    print('\033[1m' + "TIC TAC TOE GAME\n" + '\033[1m')
    print('\033[1m' + "PLAYER 1(X) & PLAYER 2(O)" + '\033[1m')
    print("\n")
    print("|   |   |   |")
    print("| {} | {} | {} |".format(square[1],square[2],square[3]))
    print("|   |   |   |")
    print("--------------")
    
    print("|   |   |   |")
    print("| {} | {} | {} |".format(square[4],square[5],square[6]))
    print("|   |   |   |")
    print("--------------")
    
    print("|   |   |   |")
    print("| {} | {} | {} |".format(square[7],square[8],square[9]))
    print("|   |   |   |")
    print("\n")

#to check for the win condition
'''
statusCode = 0  - game is not finish yet
statusCode = 1  - game is finish with a result that who's player is win
statusCode = -1 - game is finish without result, match draw
'''
def checkForWin():
    statusCode = 0
    if square[1] == square[2] and square[2] == square[3]:
        statusCode = 1
    elif square[4] == square[5] and square[5] == square[6]:
        statusCode = 1
    elif square[7] == square[8] and square[8] == square[9]:
        statusCode = 1
    elif square[1] == square[4] and square[4] == square[7]:
        statusCode = 1
    elif square[2] == square[5] and square[5] == square[8]:
        statusCode = 1
    elif square[3] == square[6] and square[6] == square[9]:
        statusCode = 1
    elif square[1] == square[5] and square[5] == square[9]:
        statusCode = 1
    elif square[3] == square[5] and square[5] == square[7]:
        statusCode = 1
    elif square[1] != 1 and square[2] != 2 and square[3] != 3 and square[4] != 4 and square[5] != 5 and square[6] != 6 and square[7] != 7 and square[8] != 8 and square[9] != 9:
        statusCode = -1
    
    return statusCode


#to update dashboard with 'X's or 'O's at their choosen position
def updateDashboard(choice,mark):
    global player
    if choice == 1 and square[1] == 1:
        square[1] = mark
    elif choice == 2 and square[2] == 2:
        square[2] = mark
    elif choice == 3 and square[3] == 3:
        square[3] = mark
    elif choice == 4 and square[4] == 4:
        square[4] = mark
    elif choice == 5 and square[5] == 5:
        square[5] = mark
    elif choice == 6 and square[6] == 6:
        square[6] = mark
    elif choice == 7 and square[7] == 7:
        square[7] = mark
    elif choice == 8 and square[8] == 8:
        square[8] = mark
    elif choice == 9 and square[9] == 9:
        square[9] = mark
    else:
        print("\nInvaild Choice.")
        player = player - 1
        time.sleep(1)

import os
import time
import color
square = list(range(10))
player = 1
result = 0
while result == 0:
    viewDashboard()
    player = 2 if player%2 == 0 else 1
    choice = int(input(f"Player {player}, Enter the position no. : "))
    mark = 'X' if player == 1 else 'O'
    player += 1
    updateDashboard(choice,mark)
    result = checkForWin()
    if result == 1:
        player -= 1
        print('\033[1m' + "\nHURRY !! PLAYER {} WINS THE MATCH.".format(player)  + '\033[1m')
        break 
else :
    print('\033[1m' + "\nMATCH DRAW !!" + '\033[1m')

time.sleep(2)

