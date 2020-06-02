	


'''

Basic Tic Tac Toe game - Chris Gleason 2015

'''

from sys import exit
from random import randint


whowon = 'no'
coords = [ [ '[1]' , '[2]' , '[3]'] , [ '[4]' ,'[5]' , '[6]' ] , [ '[7]' , '[8]' , '[9]' ] ]


def is_available(coords):

    """

    @param(string) -- a coord from the coords array
    @return(boolean) -- True if the square is empty
                     -- False if the square is occupied
    """

    return coords != "[X]" and coords != "[O]"

def print_board():

    '''
    Function to print out the Tic Tac Toe Matrix
    '''

    print (' This is the board represented as a grid of the co-ordinates ')
    print ('''
    ''')


    print ('' , coords[0][0] , '\t' , coords[0][1] , '\t' , coords[0][2])
    print ('' , coords[1][0] , '\t' , coords[1][1] , '\t' , coords[1][2])
    print ('' , coords[2][0] , '\t' , coords[2][1] , '\t' , coords[2][2])
    print ('')

def wincondition():

    '''
    This Fucntion defines wether a player has won and if so who has won before allowing
    execution of the playturn function. It also decides if there is a tie.
    '''

    if coords[0][0] == "[X]" and coords [0][1] == "[X]" and coords[0][2] == "[X]":
        iswon = True
        whowon = 'player'

    elif coords[1][0] == "[X]" and coords [1][1] == "[X]" and coords[1][2] == "[X]":
        iswon = True
        whowon = 'player'

    elif coords[2][0] == "[X]" and coords [2][1] == "[X]" and coords[2][2] == "[X]":
        iswon = True
        whowon = 'player'

    elif coords[0][0] == "[X]" and coords [1][0] == "[X]" and coords[2][0] == "[X]":
        iswon = True
        whowon = 'player'

    elif coords[0][1] == "[X]" and coords [1][1] == "[X]" and coords[2][1] == "[X]":
        iswon = True
        whowon = 'player'

    elif coords[0][2] == "[X]" and coords [1][2] == "[X]" and coords[2][2] == "[X]":
        iswon = True
        whowon = 'player'

    elif coords[0][0] == "[X]" and coords [1][1] == "[X]" and coords[2][2] == "[X]":
        iswon = True
        whowon = 'player'

    elif coords[0][2] == "[X]" and coords [1][1] == "[X]" and coords[2][0] == "[X]":
        iswon = True
        whowon = 'player'

    elif coords[0][0] == "[O]" and coords [0][1] == "[O]" and coords[0][2] == "[O]":
        iswon = True
        whowon = 'computer'

    elif coords[1][0] == "[O]" and coords [1][1] == "[O]" and coords[1][2] == "[O]":
        iswon = True
        whowon = 'computer'

    elif coords[2][0] == "[O]" and coords [2][1] == "[O]" and coords[2][2] == "[O]":
        iswon = True
        whowon = 'computer'

    elif coords[0][0] == "[O]" and coords [1][0] == "[O]" and coords[2][0] == "[O]":
        iswon = True
        whowon = 'computer'

    elif coords[0][1] == "[O]" and coords [1][1] == "[O]" and coords[2][1] == "[O]":
        iswon = True
        whowon = 'computer'

    elif coords[0][2] == "[O]" and coords [1][2] == "[O]" and coords[2][2] == "[O]":
        iswon = True
        whowon = 'computer'

    elif coords[0][0] == "[O]" and coords [1][1] == "[O]" and coords[2][2] == "[O]":
        iswon = True
        whowon = 'computer'

    elif coords[0][2] == "[O]" and coords [1][1] == "[O]" and coords[2][0] == "[O]":
        iswon = 'yes'
        whowon = 'computer'

    else:
        iswon = False

    if iswon == True:
        print ('The game is over! ' ,  whowon , ' won!')
        exit(0)

    if coords[0][0] != "[1]" and coords[0][1] != "[2]" and coords [0][2] != "[3]" \
    and coords[1][0] != "[4]" and coords[1][1] != "[5]" and coords [1][2] != "[6]" \
    and coords[2][0] != "[7]" and coords[2][1] != "[8]" and coords [2][2] != "[9]":
        print('The game is a tie!')
        exit(0) 


def playturn():

    '''
    This Function adds logic to the players turn to decide wether or not
    the space is taken or or not and marks the grid accordingly
    '''

    wincondition()
    goodroll = 'no'
    while goodroll != 'yes':
        playerchoice = input ('Which co-ordinate would you like to mark?')

        if playerchoice == "1" and coords[0][0] == "[1]":
            coords[0][0] = "[X]"
            goodroll = 'yes'

        elif playerchoice == "2" and coords[0][1] == "[2]":
            coords[0][1] = "[X]"
            goodroll = 'yes'

        elif playerchoice == "3" and coords[0][2] == "[3]":
            coords[0][2] = "[X]"
            goodroll = 'yes'

        elif playerchoice == "4" and coords[1][0] == "[4]":
            coords[1][0] = "[X]"
            goodroll = 'yes'

        elif playerchoice == "5" and coords[1][1] == "[5]":
            coords[1][1] = "[X]"
            goodroll = 'yes'

        elif playerchoice == "6" and coords[1][2] == "[6]":
            coords[1][2] = "[X]"
            goodroll = 'yes'

        elif playerchoice == "7" and coords[2][0] == "[7]":
            coords[2][0] = "[X]"
            goodroll = 'yes'

        elif playerchoice == "8" and coords[2][1] == "[8]":
            coords[2][1] = "[X]"
            goodroll = 'yes'

        elif playerchoice == "9" and coords[2][2] == "[9]":
            coords[2][2] = "[X]"
            goodroll = 'yes'

        else:
            print('None of those coordiantes are available!')

def compturn():

    '''
    This function adds decision logic to the computers turn, picks a random number
    and keeps looping until it picks a valid unchosen spot on the grid.
    '''

    wincondition()
    goodroll = False
    while not goodroll:
        choice1 = randint(0,2)
        choice2 = randint(0,2)
        if is_available(coords[choice1][choice2]):
            coords[choice1][choice2] = "[O]"
            goodroll = True

    print('Computer chose co-ordinates: ', choice1 , ',' , choice2 )

print ('Welcome to tic tac toe!')
print ('You are X and the computer is O')

while whowon != True:
    print ('''
    ''')
    print_board()
    playturn()
    compturn()
