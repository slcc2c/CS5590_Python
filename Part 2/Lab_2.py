import string

#Task 1:
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

#Task 2:
#Write a Python program to check if a string contains all letters of the alphabet

def entire_alphabet(str):
	if len(str)<26:
		return False
	letters = list(string.ascii_uppercase)
	for char in str:
		letters.remove(string.capwords(char))
		if len(letters)==0:
			return True
	return False 
print(entire_alphabet(string.ascii_lowercase))
print(entire_alphabet(string.ascii_uppercase))
print(entire_alphabet("Thiswillreturnfalse"))