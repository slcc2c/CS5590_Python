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

#declare function
def ascii_initial():
        #index to determine where we are in the letter
    row = 0
    #string patterns for the letter
    first= ' ****'
    middle = '*    '
    #outer loop
    while(row<7):
                #logic to determine which pattern to use based on index value
        if(row==0):
            print(first)
        elif(0<row<3):
            print(middle)
        elif(row==3):
            print(' *** ')
        elif(3<row<6):
              #the index notation [::-1] will reverse the string
            print(middle[::-1])
        else:
            print(first[::-1])
        #increment the index
        row += 1
#run the function        
ascii_initial()

#Task 2:
#Write a Python program to check if a string contains all letters of the alphabet

def entire_alphabet(str):
    #determine if str is too short to contain entire alphabet, save time
    if len(str)<26:
        return False
    #store alphabet as a list
    letters = list(string.ascii_uppercase)
    #loop over the characters in our string
    for char in str:
        #if the character(in any case) hasn’t been encountered yet remove it from the list
        letters.remove(string.capwords(char))
        #if all characters have been removed then every letter of the alphabet has been looped over
        if len(letters)==0:
            return True
    return False 
print(entire_alphabet(string.ascii_lowercase))
print(entire_alphabet(string.ascii_uppercase))
print(entire_alphabet("Thiswillreturnfalse"))

#Task 3:
#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

def nums_w_conditions():
    #This algorithm seeks out the first number w/ the specified properties using a slow loop then uses the properties of divisibility to quickly generate the others w/ a faster loop
    print("Finding first #")
    #does number fit range rules
    for i in range(1501,2700,1):
        #does number fit divisibility rules
        if(i%5==0 and i%7==0):
            #number has been found go to next loop
            break
        else:
            continue
    #since 5/7 are co-prime we can take a number N that fits the properties and generate the rest by taking N+k*5*7 in the interval
    for j in range(i,2700,35):
        #display each number and validate it meets the conditions, the interval condition can be verified visually
        print(j," :", i%5==0 and i%7==0)
nums_w_conditions()
