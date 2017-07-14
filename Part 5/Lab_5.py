# 1
class Person:
    # init
    def __init__(self, obj_name):
        self.name = obj_name
        self._role = 'No Role'


# inheritance
class Employee(Person):
    # init
    def __init__(self, obj_name, home, job):
        self.job = job
        # instance or person
        Person.__init__(self, obj_name)
        self.hometown = home
        self._role = 'Employee'

    def change_name(self, new_name):
        super().name = new_name


class FlightRoute():
    # init
    def __init__(self, origin, dest):
        self.dest = dest
        self.origin = origin


class Flight(FlightRoute):
    # init
    def __init__(self, flight, origin, dest):
        # instance of flightroute
        FlightRoute.__init__(self, origin, dest)
        self.flight = flight


# double inheritance
class Passenger(Person, Flight):
    # init
    def __init__(self, obj_name, home, dest, flight):
        Person.__init__(self, obj_name)
        self._role = 'Passenger'
        # instance of flight
        Flight.__init__(self, flight, home, dest)


# 5 classes
# Used self
# role is private

# 2)
class TicTacToe():
    # track status of game
    game_over = False
    # hold board in 1D list
    board = []
    # track num of moves in game
    moves = 0;

    # initialize game
    def __init__(self, l, w):
        self.rows = l
        self.cols = w
        for i in range(l * w):
            self.board.append('-')
        self.game()

    def print_horiz_line(self, size):
        print("--" * size)

    def print_vert_line(self, size):
        print("|\t" * size)

    # print board
    def game_board(self, size, spaces):
        for i in range(size):
            self.print_horiz_line(size + 1)
            self.print_vert_line(size + 1)
        self.print_horiz_line(size + 1)

    # perform checks of rows,cols, and diags
    def check_winner(self, player):
        for i in range(self.cols):
            temp = True
            for j in range(self.rows):
                if self.board[(j * self.cols) + i] != player:
                    temp = False
                    break
            if temp:
                self.game_over = True
                break
        for i in range(self.rows):
            temp = True
            for j in range(self.cols):
                if self.board[(i * self.cols) + j] != player:
                    temp = False
                    break
            if temp:
                self.game_over = True
                break
        for i in range(min(self.rows, self.cols)):
            temp = True
            temp_alt = True
            if self.board[(i * self.cols) + i] != player:
                temp = False
            if self.board[(i * self.cols) + (self.cols - i)] != player:
                temp_alt = False
        self.game_over = temp or temp_alt

    # main game logic
    def game(self):
        while (not self.game_over):
            print('Move ', self.moves, " Player", (self.moves % 2) + 1, "'s turn: ")
            for i in range(self.rows):
                self.print_horiz_line(self.cols)
                temp = ''
                for j in range(self.cols):
                    temp += '|'
                    temp += self.board[(i * self.cols) + j]
                temp += '|'
                print(temp)
            self.print_horiz_line(self.cols)
            print('\n')
            valid = False
            while not valid:
                move = input("Player " + str((self.moves % 2) + 1) + " please enter your move as row,col: ")
                coords = move.split(',')
                coords[0] = int(coords[0])
                coords[1] = int(coords[1])
                if (self.board[(coords[0] * self.cols) + coords[1]] == '-'):
                    valid = True
            if ((self.moves % 2) == 0):
                self.board[(coords[0] * self.cols) + coords[1]] = 'X'
                self.check_winner('X')
            else:
                self.board[(coords[0] * self.cols) + coords[1]] = 'O'
                self.check_winner('O')
            self.moves += 1
            if self.moves == (self.rows * self.cols):
                self.game_over = True
        for i in range(self.rows):
            self.print_horiz_line(self.cols)
            temp = ''
            for j in range(self.cols):
                temp += '|'
                temp += self.board[(i * self.cols) + j]
            temp += '|'
            print(temp)
        self.print_horiz_line(self.cols)
        if self.moves == (self.rows * self.cols):
            print("Tie Game")
        else:
            if ((self.moves % 2) == 0):
                print('O is the winner')
            else:
                print('X is the winner')


game = TicTacToe(3,3)

# 3)
import numpy as np


class GameOfLife:
    nums = np.random.rand(10, 10)

    def __init__(self):
        for i in range(10):
            for j in range(10):
                if self.nums[i, j] <= .5:
                    self.nums[i, j] = 0.0
                else:
                    self.nums[i, j] = 1.0
        self.game()

    def generate_indices(self, x, y):
        indices = []
        x_temp = x
        y_temp = y
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j and i == 0:
                    continue
                x_temp = x + i
                y_temp = y + j
                if (-1 < x_temp < 10) and (-1 < y_temp < 10):
                    indices.append((x_temp, y_temp))
        return indices

    def live_count(self, i, j):
        live_count = 0
        indices = self.generate_indices(i, j)
        for coord in indices:
            if live_count > 3:
                break
            value = self.nums[coord[0], coord[1]]
            if value == 1.0:
                live_count += 1
        return live_count

    def rule_1(self, count):
        return count > 3

    def rule_2(self, count):
        return count == 2 or count == 3

    def rule_3(self, count):
        return count < 2

    def rule_4(self, surrounding_count):
        temp = surrounding_count == 3
        return temp

    def game(self):
        print(self.nums)
        while (True):
            for i in range(10):
                for j in range(10):
                    value = self.nums[i, j]
                    count = self.live_count(i, j)
                    num_surrounding = len(self.generate_indices(i, j))
                    if self.rule_1(count):
                        self.nums[i, j] = 0.0

                    elif self.rule_2(count):
                        self.nums[i, j] = self.nums[i, j]

                    elif self.rule_3(count):
                        self.nums[i, j] = 0.0

                    if self.rule_4(num_surrounding) and (value == 0.0):
                        self.nums[i, j] = 1.0
                        continue
            print(self.nums)


conway = GameOfLife()
