#1)
def toList():
    word = input('Please input a word')
    print(list(word),'\n',tuple(word))

toList()
#2)
def listOfTuples():
    user_input = ''
    l=[]
    while(user_input != 'q'):
        user_input = input('enter first number')
        temp = user_input
        user_input = input('enter second number or type q to stop')
        l.append((temp,user_input))
    return sorted(l[:len(l)-1], key=lambda x:x[1])
print(listOfTuples())

#3)
def print_horiz_line(size):
    print("--"*size)
def print_vert_line(size):
    print("|\t" * size)
def game_board(size, spaces):
    for i in range(size):
        print_horiz_line(size+1)
        print_vert_line(size+1)
    print_horiz_line(size+1)


def TTT():
    game_over = False
    board = []
    moves = 0;
    for i in range(9):
        board.append('-')
    while(not game_over):
        print('Move ',moves," Player",(moves%2)+1,"'s turn: ")
        for i in range(3):
            print_horiz_line(3)
            temp = ''
            for j in range(3):
                temp += '|'
                temp += board[(i*3) + j]
            temp+='|'
            print(temp)
        print_horiz_line(3)
        print('\n')

        valid=False
        while(not valid):
            move = input("Player "+str((moves%2)+1)+ " please enter your move as row,col: ")
            coords = move.split(',')
            coords[0] = int(coords[0])
            coords[1] = int(coords[1])
            if(board[(coords[0]*3)+coords[1]] == '-'):
                valid = True
        if((moves%2)==0):
            board[(coords[0] * 3) + coords[1]] = 'X'
        else:
            board[(coords[0] * 3) + coords[1]] = 'O'
        moves+=1
        if('-' not in board):
            game_over = True

TTT()