__author__ = 'Manan Chetan Buddhadev'

"""
minStepsInfGrid.py

You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

author: Manan Chetan Buddhadev
"""

class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):

        # Initializing Values
        numberOfSteps = 0

        currentX = X[0] # Starting X co-ordinate
        currentY = Y[0] # Starting Y co-ordinate

        for i in range(1, len(X)) :
            numberOfSteps += max(abs(currentX - X[i] ), abs(currentY - Y[i])) #
            currentX = X[i]
            currentY = Y[i]
        return numberOfSteps

def main():
    X=[4,8,-7,-5,-13,-9,-7,8]
    Y=[4,8,-7,-5,-13,-9,-7,8]
    Solution.coverPoints()