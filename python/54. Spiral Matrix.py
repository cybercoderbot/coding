"""
54. Spiral Matrix
Medium

8042

876

Add to List

Share
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        # Simulate the path to visit the elements.
        Time complexity O(MN)
        Space complexity O(1)
        """
        res = []
        i = j = 0
        di, dj = 0, 1
        M, N = len(matrix), len(matrix[0])

        for _ in range(M * N):
            res.append(matrix[i][j])
            matrix[i][j] = None
            if not (0 <= i+di < M and 0 <= j+dj < N and matrix[i+di][j+dj]):
                di, dj = dj, -di
            i += di
            j += dj

        return res
