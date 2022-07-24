"""
59. Spiral Matrix II
Medium


Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
"""


class Solution:
    def generateMatrix(self, N: int) -> List[List[int]]:
        """
        Generate numbers from 1 to N^2 and fill them in the proper position in the matrix.
        Time complexity O(N^2)
        Space complexity O(N^2)

        """
        i = j = 0
        di, dj = 0, 1
        res = [[0]*N for _ in range(N)]

        for x in range(1, N*N+1):
            res[i][j] = x
            if res[(i+di) % N][(j+dj) % N]:
                di, dj = dj, -di
            i, j = i+di, j+dj

        return res
