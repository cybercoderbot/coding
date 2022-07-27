"""
240. Search a 2D Matrix II
Medium

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
"""


"""
Starting from the top-right corner, at any place i, j, compare matrix[i][j] with target.

if matrix[i][j] == target, return True
if matrix[i][j] < target, increment i
if matrix[i][j] > target decrement j.
If i, j falls outside of range, return False.

"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time complexity O(max(M, N))
        Space complexity O(1)
        """
        M, N = len(matrix), len(matrix[0])
        i, j = 0, N-1

        while i < M and 0 <= j:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1

        return False
