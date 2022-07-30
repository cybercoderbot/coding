"""
766. Toeplitz Matrix
Easy

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M, N = len(matrix), len(matrix[0])
        for i, j in product(range(M-1), range(N-1)):
            if matrix[i+1][j+1] != matrix[i][j]:
                return False
        return True


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M, N = len(matrix), len(matrix[0])
        for i, j in product(range(M), range(N)):
            k = min(i, j)
            if matrix[i][j] != matrix[i-k][j-k]:
                return False
        return True
