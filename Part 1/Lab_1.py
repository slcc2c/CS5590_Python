#1 Check whether a number input by the user is even or odd
def check_input():
    #if input is divisible by 2 number must be even
    if int(input("Number?"))%2 is 0:
        return "even"
    else:
        return "odd"
#run function
print(check_input())

#2 Take length and breadth of a rectangle from user and print perimeter of the same.
def perimeter(length, breadth):
    return 2*length+2*breadth
print(perimeter(int(input("length?")),int(input("breadth?"))))

#3 This is a number guess exercise. First pick a random digit via program i.e 0,1,2,3,4,5,6,7,8,9
import random
def guessing_game():
    print("This game will generate a random digit 0,..,9 then ask you to guess it, if your guess is wrong it will tell you if you were too low or too high ")
    guess = int(input("Please guess a digit..."))
    num = random.randrange(0,10)
    if guess == num:
        return "perfect"
    elif guess < num:
        return "too small, number was:"+str(num)
    else:
        return "too large, number was:"+str(num)

print(guessing_game())