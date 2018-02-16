from State import *
import copy

class Utils:

    def evaluate(self, grid):
        grid = grid.get_grid()

        # Check Rows
        for row in range(3):
            if grid[row][0] == grid[row][1] and grid[row][1] == grid[row][2]:
                if grid[row][0] == "X":
                    return 10
                elif grid[row][0] == "O":
                    return -10

        # Check Columns
        for columns in range(3):
            if grid[0][columns] == grid[1][columns] and grid[1][columns] == grid[2][columns]:
                if grid[0][columns] == "X":
                    return 10
                elif grid[0][columns] == "O":
                    return -10

        # Check Diagonals
        if grid[0][0] == grid[1][1] and grid[1][1] == grid [2][2]:
            if grid[0][0] == 'X':
                return 10
            elif grid[0][0] == 'O':
                return -10
        if grid[0][2] == grid[1][1] and grid[1][1] == grid [2][0]:
            if grid[0][2] == 'X':
                return 10
            elif grid[0][2] == 'O':
                return -10

        return 0

    def getPossibleMove(self, grid, isMaximizingPlayer):
        newGrid = copy.deepcopy(grid)
        originalGrid = copy.deepcopy(grid)
        possibleMove = []

        if isMaximizingPlayer == 1:
            for row in range(3):
                for columns in range(3):
                    if (originalGrid.get_grid()[row][columns] == '_'):
                        newGrid.get_grid()[row][columns] = 'X'
                        possibleMove.append(newGrid)
                        newGrid = copy.deepcopy(originalGrid)
            return possibleMove

        elif isMaximizingPlayer == -1:
            for row in range(3):
                for columns in range(3):
                    if (originalGrid.get_grid()[row][columns] == '_'):
                        newGrid.get_grid()[row][columns] = 'O'
                        possibleMove.append(newGrid)
                        newGrid = copy.deepcopy(originalGrid)
            return possibleMove

    def putXorOinLastBox(self, grid, mark):
        for row in range(3):
            for columns in range(3):
                if (grid.get_grid()[row][columns] == '_'):
                    grid.get_grid()[row][columns] = mark
                    break
        return grid

    def checkIfTerminalState(self, grid):
        grid = grid.get_grid()

        # Check Rows
        for row in range(3):
            if grid[row][0] == grid[row][1] and grid[row][1] == grid[row][2]:
                if grid[row][0] != '_':
                    return True

        # Check Columns
        for columns in range(3):
            if grid[0][columns] == grid[1][columns] and grid[1][columns] == grid[2][columns]:
                if grid[0][columns] != '_':
                    return True

        # Check Diagonals
        if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
            if grid[0][0] != '_':
                return True

        if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
            if grid[0][2] != '_':
                return True

        count = 0
        for row in range(3):
            for columns in range(3):
                if (grid[row][columns] == 'X' or grid[row][columns] == 'O'):
                    count += 1
        if count == 9:
            return True

        return False

# utils = Utils()
# grid = State.factory("Custom")

# grid.display_grid()
# grid.get_grid()[0][0] = 'X'
# grid.display_grid()

# a = utils.getPossibleMove(grid, 1)
# print(len(a))
# score = [utils.evaluate(grid) for grid in a]
# print(score)
