"""
498. Diagonal Traverse
Medium

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
"""


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []  # edge case

        res = []
        M, N = len(matrix), len(matrix[0])  # dimension
        i = j = 0
        for _ in range(M * N):
            res.append(matrix[i][j])
            if (i+j) % 2 == 0:  # moving up
                if j == N-1:
                    i += 1
                elif i == 0:
                    j += 1
                else:
                    i, j = i-1, j+1
            else:
                if i == M-1:
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    i, j = i+1, j-1
        return res
