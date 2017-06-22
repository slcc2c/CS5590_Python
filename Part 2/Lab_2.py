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

#Task 3:
#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

def nums_w_conditions():
	print("Finding first #")
	for i in range(1501,2700,1):
		if(i%5==0 and i%7==0):
			break
		else:
			continue
	for j in range(i,2700,35):
		print(j," :", i%5==0 and i%7==0)
nums_w_conditions()