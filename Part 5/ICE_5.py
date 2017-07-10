import random

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_name_salary(self):
        print(self.name, self.salary)

num_employees = 0

def count_num_employees():
    return num_employees

def display_name_salary(employee):
    print(employee.salary, employee.name)



class Manager(Employee):

    def __init__(self, name, salary):
        is_manager = True
        self.name = name
        self.salary = salary

emp = Employee('spencer',500)
manager = Manager('spencer',500)

min = -1
max = -1
nums = []

for i in range(10):
    nums.append([])
    for j in range(10):
        rand = random.randrange(0,1000)
        nums[i].append(rand)
        if rand > max:
            max=rand
        if rand < min:
            min=rand
print(max,min)


