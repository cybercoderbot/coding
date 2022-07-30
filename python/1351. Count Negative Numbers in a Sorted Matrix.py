"""
1351. Count Negative Numbers in a Sorted Matrix
Easy

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0
"""


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        xyrange = product(range(M), range(N))
        return sum([1 for i, j in xyrange if grid[i][j] < 0])


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        return sum([1 for i, j in product(range(M), range(N)) if grid[i][j] < 0])


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for row in grid:
            for x in row:
                if x < 0:
                    res += 1
        return res


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        count = 0
        for i, j in product(range(row), range(col)):
            if grid[i][j] < 0:
                count += 1
        return count
