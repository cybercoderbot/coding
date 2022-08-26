"""
73. Set Matrix Zeroes
Medium

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Solution: to use set to record in which row and col appears 0
        Time Complexity : O(MN)
        Space: O(M+N) 
        """
        M, N = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for i, j in product(range(M), range(N)):
            if not matrix[i][j]:
                rows.add(i)
                cols.add(j)

        for i, j in product(range(M), range(N)):
            if i in rows or j in cols:
                matrix[i][j] = 0
        return
