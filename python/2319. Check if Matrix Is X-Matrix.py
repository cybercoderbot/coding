"""
2319. Check if Matrix Is X-Matrix
Easy

A square matrix is said to be an X-Matrix if both of the following conditions hold:

All the elements in the diagonals of the matrix are non-zero.
All other elements are 0.
Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.

Example 1:
Input: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
Output: true
Explanation: Refer to the diagram above. 
An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
Thus, grid is an X-Matrix.

Example 2:
Input: grid = [[5,7,0],[0,3,1],[0,5,0]]
Output: false
Explanation: Refer to the diagram above.
An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
Thus, grid is not an X-Matrix.
"""


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        N = len(grid)
        for i, j in product(range(N), range(N)):
            if i == j or i+j == N-1:
                if grid[i][j] == 0:
                    return False
            else:
                if grid[i][j]:
                    return False
        return True


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        N = len(grid)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if (i == j or i+j == N-1) and not x:
                    return False
                if i != j and i+j != N-1 and x:
                    return False
        return True


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        N = len(grid)
        for i, j in product(range(N), range(N)):
            if (i == j or i+j == N-1) and not grid[i][j]:
                return False
            if i != j and i+j != N-1 and grid[i][j]:
                return False
        return True
