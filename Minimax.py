from State import *
from Utils import *

class Minimax:

    def __init__(self):
        self.utils = Utils()

    def findBestMove(self, grid):

        newGrid = copy.deepcopy(grid)
        originalGrid = copy.deepcopy(grid)
        bestValue = -99999
        bestRowMove = 0
        bestColumnsMove = 0

        for row in range(3):
            for columns in range(3):
                if originalGrid.get_grid()[row][columns] == '_':
                    newGrid.get_grid()[row][columns] = 'X' # Assuming X is maximizer, after he makes the move,
                    evaluationValue = self.minimax(newGrid, 0, -1) # it will be O turn.
                    print("yo {}".format(evaluationValue))
                    newGrid = copy.deepcopy(originalGrid) # Reset grid to Original
                    if evaluationValue > bestValue:
                        bestRowMove = row
                        bestColumnsMove = columns
                        bestValue = evaluationValue

        print("The best row to move is {}".format(bestRowMove))
        print("The best column to move is {}".format(bestColumnsMove))

    def minimax(self, grid, depth, isMaximizingPlayer):

        newGrid = copy.deepcopy(grid)
        originalGrid = copy.deepcopy(grid)

        # if depth == 9:
        #     if isMaximizingPlayer == 1:
        #         newGrid = self.utils.putXorOinLastBox(newGrid, 'X')
        #     elif isMaximizingPlayer == -1:
        #         newGrid = self.utils.putXorOinLastBox(newGrid, 'O')
        #     newGrid.display_grid()
        #     print("Evaluation value: {}".format(self.utils.evaluate(newGrid)))
        #     return self.utils.evaluate(newGrid)

        if self.utils.checkIfTerminalState(newGrid) == True:
            newGrid.display_grid()
            print("Evaluation value: {}".format(self.utils.evaluate(newGrid)))
            return self.utils.evaluate(newGrid)

        if isMaximizingPlayer == 1:
            bestValue = -99999
            for row in range(3):
                for columns in range(3):
                    if (originalGrid.get_grid()[row][columns] == '_'):
                        newGrid.get_grid()[row][columns] = 'X'
                        value = self.minimax(newGrid, depth + 1, -isMaximizingPlayer)
                        newGrid = copy.deepcopy(originalGrid) # Reset grid to Original
                        bestValue = max(bestValue, value)
                        print("Best current value for Maximizing Player: {}".format(bestValue))
            return bestValue

        elif isMaximizingPlayer == -1:
            bestValue = 99999
            for row in range(3):
                for columns in range(3):
                    if (originalGrid.get_grid()[row][columns] == '_'):
                        newGrid.get_grid()[row][columns] = 'O'
                        value = self.minimax(newGrid, depth + 1, -isMaximizingPlayer)
                        newGrid = copy.deepcopy(originalGrid) # Reset grid to Original
                        bestValue = min(bestValue, value)
                        print("Best current value for Minimizing Player: {}".format(bestValue))
            return bestValue

#
# # myMinimax.minimax(grid, 1, 1)
# print(myMinimax.oneLevel(grid, 1, -1))

# utils = Utils()

grid = State.factory("Custom")
myMinimax = Minimax()
# print(myMinimax.minimax(grid, 8, 1))

myMinimax.findBestMove(grid)