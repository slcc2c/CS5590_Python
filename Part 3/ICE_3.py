#Problem 1

def print_horiz_line(size):
    print("---"*size)
def print_vert_line(size):
    print("|\t" * size)
def game_board(size):
    for i in range(size):
        print_horiz_line(size+1)
        print_vert_line(size+1)
    print_horiz_line(size+1)

game_board(3)

#Problem 2
def first_last(nums):
    return [nums[0],nums[len(nums)-1]]
print(first_last([1,3,4,5,6,7]))