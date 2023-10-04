#make the board blank in the 2D Array
def make_board():
    print()
    for i in range(0,3):
        print(' '.join(board[i]))
    print()
#control scheme
def make_controls():
    print()
    for i in range(0,3):
        print(' '.join(controls[i]))
    print()
#placing x's or o's in the array
def place_x(r,c):
    if board[r][c]=='-':
        board[r][c]='x'
    else:
        redo = int(input("Enter a valid space: "))
        place_x(controller(redo)[0],controller(redo)[1])
def place_o(r,c):
    if board[r][c]=='-':
        board[r][c]='o'
    else:
        redo = int(input("Enter a valid space: "))
        place_o(controller(redo)[0],controller(redo)[1])

#control scheme handling
def controller(num):
    match num:
        case 1:
            return [0,0]
        case 2:
            return [0,1]
        case 3:
            return [0,2]
        case 4:
            return [1,0]
        case 5:
            return [1,1]
        case 6:
            return [1,2]
        case 7:
            return [2,0]
        case 8:
            return [2,1]
        case 9:
            return [2,2]
        case 99:
            done = True

board = [["-","-","-"],["-","-","-"],["-","-","-"]]
controls = [["1","2","3"],["4","5","6"],["7","8","9"]]
done = False
winner = ""

while not done:
    make_controls()
    print("This is the numbering scheme for inputs")
    user_place = int(input("P1: Enter which space you would like to go: "))
    place_x(controller(user_place)[0],controller(user_place)[1])
    make_board()
    for i in range(0,3):
        if board[i][0]=="x" and board[i][1]=="x" and board[i][2]=="x":
            winner = "P1"
            print(winner+" has won the game!")
            done = True
        if board[0][i]=="x" and board[1][i]=="x" and board[2][i]=="x":
            winner = "P1"
            print(winner+" has won the game!")
            done = True
        if board[i][0]=="o" and board[i][1]=="o" and board[i][2]=="o":
            winner = "P2"
            print(winner+" has won the game!")
            done = True
        if board[0][i]=="o" and board[1][i]=="o" and board[2][i]=="o":
            winner = "P2"
            print(winner+" has won the game!")
            done = True
        if board[0][0]=="o" and board[1][1]=="o" and board[2][2]=="o":
            winner = "P2"
            print(winner+" has won the game!")
            done = True
        if board[0][0]=="x" and board[1][1]=="x" and board[2][2]=="x":
            winner = "P1"
            print(winner+" has won the game!")
            done = True
        if board[0][2]=="o" and board[1][1]=="o" and board[2][0]=="o":
            winner = "P2"
            print(winner+" has won the game!")
            done = True
        if board[0][2]=="x" and board[1][1]=="x" and board[2][0]=="x":
            winner = "P1"
            print(winner+" has won the game!")
            done = True
    make_controls()
    print("This is the numbering scheme for inputs")
    user_place = int(input("P2: Enter which space you would like to go: "))
    place_o(controller(user_place)[0],controller(user_place)[1])
    make_board()
    for i in range(0,3):
        if board[i][0]=="x" and board[i][1]=="x" and board[i][2]=="x":
            winner = "P1"
            print(winner+" has won the game!")
            done = True
        if board[0][i]=="x" and board[1][i]=="x" and board[2][i]=="x":
            winner = "P1"
            print(winner+" has won the game!")
            done = True
        if board[i][0]=="o" and board[i][1]=="o" and board[i][2]=="o":
            winner = "P2"
            print(winner+" has won the game!")
            done = True
        if board[0][i]=="o" and board[1][i]=="o" and board[2][i]=="o":
            winner = "P2"
            print(winner+" has won the game!")
            done = True
        if board[0][0]=="o" and board[1][1]=="o" and board[2][2]=="o":
            winner = "P2"
            print(winner+" has won the game!")
            done = True
        if board[0][0]=="x" and board[1][1]=="x" and board[2][2]=="x":
            winner = "P1"
            print(winner+" has won the game!")
            done = True
        if board[0][2]=="o" and board[1][1]=="o" and board[2][0]=="o":
            winner = "P2"
            print(winner+" has won the game!")
            done = True
        if board[0][2]=="x" and board[1][1]=="x" and board[2][0]=="x":
            winner = "P1"
            print(winner+" has won the game!")
            done = True
#some of this was done pretty strangely and could definitley be optimized
#if this did not already take a few hours i would have:
#-changed win state checking of the game to pattern matching not explicit checking
#-added code to stop when the game has reached a tie, it's harder than I orignally 
# thought to deduce when a game is definitely a tie and I could not gain any ground on that
# if I had some more time I was going to just keep a running count of number of 'used' spaces
# and then when the number of used spaces went higher than whatever the number of moves is,
# start checking if the game can terminate as in, run a couple checks to see if the player who
# is up still has a chance to win, if not - terminate