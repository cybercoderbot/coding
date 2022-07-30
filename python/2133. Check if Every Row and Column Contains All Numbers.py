"""
2133. Check if Every Row and Column Contains All Numbers
Easy

An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

Example 1:
Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.

Example 2:
Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
Hence, we return false.
"""


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        M, N = len(matrix), len(matrix[0])

        for i, j in product(range(M), range(N)):
            x = matrix[i][j]
            if x in (row[i] | col[j]):
                return False
            row[i].add(x)
            col[j].add(x)

        return True


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        validRow = all(len(set(row)) == len(row) for row in matrix)
        validCol = all(len(set(col)) == len(col) for col in zip(*matrix))
        return validRow and validCol
