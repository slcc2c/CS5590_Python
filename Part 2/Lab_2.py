#Write a python program that print the first letter of your name with star. You have to use the instructions in the class.
# For this you should use nested loop to implement.
#The expected output should be something like this:
#  ****
# *
# *
#  ***
#     *
#     *
# ****

def ascii_initial():
    row = 0
    first= ' ****'
    middle = '*    '
    while(row<7):

        if(row==0):
            print(first)
        elif(0<row<3):
            print(middle)
        elif(row==3):
            print(' *** ')
        elif(3<row<6):
            print(middle[::-1])
        else:
            print(first[::-1])
        row += 1
ascii_initial()
