"""
867. Transpose Matrix
Easy

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
"""


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        """
        Filling in matrix elements
        """
        M, N = len(A), len(A[0])
        B = [[0] * M for _ in range(N)]
        for i, j in product(range(M), range(N)):
            B[j][i] = A[i][j]

        return B


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        """
        using list comprehension
        """
        return [[row[j] for row in A] for j in range(len(A[0]))]


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        """
        using zip built-in function
        """
        return zip(*A)


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        """
        extending empty list
        """
        matrix = []
        for j in range(len(A[0])):
            row = []
            for i in range(len(A)):
                row.append(A[i][j])
            matrix.append(row)
        return matrix
