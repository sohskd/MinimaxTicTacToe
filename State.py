from __future__ import generators

class State:

    def factory(type):
        if type == "AllEmpty": return AllEmpty()
        elif type == "ThreeStraightHorizontal": return ThreeStraightHorizontal()
        elif type == "ThreeStraightVertical": return ThreeStraightVertical()
        elif type == "ThreeStraightSlash": return ThreeStraightSlash()
        elif type == "ThreeStraightBackSlash": return ThreeStraightBackSlash()
        elif type == "ThreeStraightHorizontalO": return ThreeStraightHorizontalO()
        elif type == "ThreeStraightVerticalO": return ThreeStraightVerticalO()
        elif type == "ThreeStraightSlashO": return ThreeStraightSlashO()
        elif type == "ThreeStraightBackSlashO": return ThreeStraightBackSlashO()
        elif type == "Custom": return Custom()

class AllEmpty(State):

    def __init__(self):
        self.name = "AllEmpty"
        self.grid = [['_', '_', '_'],
                    ['_', '_', '_'],
                    ['_', '_', '_']]

    def display_grid(self):
        print("Current grid layout :")
        print(self.grid[0][0] + '|' + self.grid[0][1] + '|' + self.grid[0][2])
        print(self.grid[1][0] + '|' + self.grid[1][1] + '|' + self.grid[1][2])
        print(self.grid[2][0] + '|' + self.grid[2][1] + '|' + self.grid[2][2])

    def display_name(self):
        print("Grid created: {}".format(self.name))

    def get_grid(self):
        return self.grid

class ThreeStraightHorizontal(State):

    def __init__(self):
        self.name = "ThreeStraightHorizontal"
        self.grid = [['X', 'X', 'X'],
                    ['_', '_', '_'],
                    ['_', '_', '_']]

    def display_grid(self):
        print("Current grid layout :")
        print(self.grid[0][0] + '|' + self.grid[0][1] + '|' + self.grid[0][2])
        print(self.grid[1][0] + '|' + self.grid[1][1] + '|' + self.grid[1][2])
        print(self.grid[2][0] + '|' + self.grid[2][1] + '|' + self.grid[2][2])

    def display_name(self):
        print("Grid created: {}".format(self.name))

    def get_grid(self):
        return self.grid

class ThreeStraightHorizontalO(State):

    def __init__(self):
        self.name = "ThreeStraightHorizontalO"
        self.grid = [['O', 'O', 'O'],
                    ['_', '_', '_'],
                    ['_', '_', '_']]

    def display_grid(self):
        print("Current grid layout :")
        print(self.grid[0][0] + '|' + self.grid[0][1] + '|' + self.grid[0][2])
        print(self.grid[1][0] + '|' + self.grid[1][1] + '|' + self.grid[1][2])
        print(self.grid[2][0] + '|' + self.grid[2][1] + '|' + self.grid[2][2])

    def display_name(self):
        print("Grid created: {}".format(self.name))

    def get_grid(self):
        return self.grid

class ThreeStraightVertical(State):

    def __init__(self):
        self.name = "ThreeStraightVertical"
        self.grid = [['X', '_', '_'],
                    ['X', '_', '_'],
                    ['X', '_', '_']]

    def display_grid(self):
        print("Current grid layout :")
        print(self.grid[0][0] + '|' + self.grid[0][1] + '|' + self.grid[0][2])
        print(self.grid[1][0] + '|' + self.grid[1][1] + '|' + self.grid[1][2])
        print(self.grid[2][0] + '|' + self.grid[2][1] + '|' + self.grid[2][2])

    def display_name(self):
        print("Grid created: {}".format(self.name))

    def get_grid(self):
        return self.grid

class ThreeStraightVerticalO(State):

    def __init__(self):
        self.name = "ThreeStraightVerticalO"
        self.grid = [['O', '_', '_'],
                    ['O', '_', '_'],
                    ['O', '_', '_']]

    def display_grid(self):
        print("Current grid layout :")
        print(self.grid[0][0] + '|' + self.grid[0][1] + '|' + self.grid[0][2])
        print(self.grid[1][0] + '|' + self.grid[1][1] + '|' + self.grid[1][2])
        print(self.grid[2][0] + '|' + self.grid[2][1] + '|' + self.grid[2][2])

    def display_name(self):
        print("Grid created: {}".format(self.name))

    def get_grid(self):
        return self.grid

class ThreeStraightSlash(State):

    def __init__(self):
        self.name = "ThreeStraightSlash"
        self.grid = [['X', '_', '_'],
                    ['_', 'X', '_'],
                    ['_', '_', 'X']]

    def display_grid(self):
        print("Current grid layout :")
        print(self.grid[0][0] + '|' + self.grid[0][1] + '|' + self.grid[0][2])
        print(self.grid[1][0] + '|' + self.grid[1][1] + '|' + self.grid[1][2])
        print(self.grid[2][0] + '|' + self.grid[2][1] + '|' + self.grid[2][2])

    def display_name(self):
        print("Grid created: {}".format(self.name))

    def get_grid(self):
        return self.grid

class ThreeStraightSlashO(State):

    def __init__(self):
        self.name = "ThreeStraightSlashO"
        self.grid = [['O', '_', '_'],
                    ['_', 'O', '_'],
                    ['_', '_', 'O']]

    def display_grid(self):
        print("Current grid layout :")
        print(self.grid[0][0] + '|' + self.grid[0][1] + '|' + self.grid[0][2])
        print(self.grid[1][0] + '|' + self.grid[1][1] + '|' + self.grid[1][2])
        print(self.grid[2][0] + '|' + self.grid[2][1] + '|' + self.grid[2][2])

    def display_name(self):
        print("Grid created: {}".format(self.name))

    def get_grid(self):
        return self.grid

class ThreeStraightBackSlash(State):

    def __init__(self):
        self.name = "ThreeStraightBackSlash"
        self.grid = [['_', '_', 'X'],
                    ['_', 'X', '_'],
                    ['X', '_', '_']]

    def display_grid(self):
        print("Current grid layout :")
        print(self.grid[0][0] + '|' + self.grid[0][1] + '|' + self.grid[0][2])
        print(self.grid[1][0] + '|' + self.grid[1][1] + '|' + self.grid[1][2])
        print(self.grid[2][0] + '|' + self.grid[2][1] + '|' + self.grid[2][2])

    def display_name(self):
        print("Grid created: {}".format(self.name))

    def get_grid(self):
        return self.grid

class ThreeStraightBackSlashO(State):

    def __init__(self):
        self.name = "ThreeStraightBackSlashO"
        self.grid = [['_', '_', 'O'],
                     ['_', 'O', '_'],
                     ['O', '_', '_']]

    def display_grid(self):
        print("Current grid layout :")
        print(self.grid[0][0] + '|' + self.grid[0][1] + '|' + self.grid[0][2])
        print(self.grid[1][0] + '|' + self.grid[1][1] + '|' + self.grid[1][2])
        print(self.grid[2][0] + '|' + self.grid[2][1] + '|' + self.grid[2][2])

    def display_name(self):
        print("Grid created: {}".format(self.name))

    def get_grid(self):
        return self.grid

class Custom(State):

    def __init__(self):
        self.name = "Custom"
        self.grid = [['X', 'O', 'X'],
                     ['_', 'O', 'O'],
                     ['_', 'X', 'O']]

    def display_grid(self):
        print("Current grid layout :")
        print(self.grid[0][0] + '|' + self.grid[0][1] + '|' + self.grid[0][2])
        print(self.grid[1][0] + '|' + self.grid[1][1] + '|' + self.grid[1][2])
        print(self.grid[2][0] + '|' + self.grid[2][1] + '|' + self.grid[2][2])

    def display_name(self):
        print("Grid created: {}".format(self.name))

    def get_grid(self):
        return self.grid

# grid = State.factory("ThreeStraightBackSlash")
# print(grid.get_grid()[0][2])
# grid.display_grid()
# grid.display_name()