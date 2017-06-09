#python 2 vs python 3
#1 in python 3 print requires parameter arguments like a function, in 2 it acts more like a statement
#2 python 2 does floor division for integers
#3 3 is still in active development, 2 is not

#reverse a number
def rev_num(num):
    #ensure number is stored as integer
    number = int(num)
    #store reversed number
    new_number = 0
    #operation is done when we are out of numbers
    while(number is not 0):
        #make room for next digit
        new_number *= 10
        #add new digit
        new_number += number%10
        #remove digit from old number
        number= number // 10
    #yeild result
    return new_number
to_reverse = input("number to reverse?")
print(rev_num(to_reverse))


#area of circle
def area_circumference(radius):
    r = int(radius)
    return (3.14*(r**2),3.14*2*r)
radius = input("radius of circle?")
result_pair = area_circumference(radius)
print("area: ",result_pair[0]," circumference: ", result_pair[1])
