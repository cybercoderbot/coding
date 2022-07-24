"""
64. Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""


"""
Approach 2 - bottom-up dp

# Define fn(i, j) as the path sum at position (i, j). Then,
# fn(0, 0) = grid[0][0],
# fn(i, j) = min(fn(i-1, j), fn(i, j-1)) + grid[i][j].

Algorithm:
Similar to approach 1 but with bottom-up implementation.
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        M, N = len(grid), len(grid[0])
        res = [inf] * N
        res[0] = 0

        for i in range(M):
            for j in range(N):
                if j:
                    res[j] = min(res[j-1], res[j])
                res[j] += grid[i][j]

        return res[-1]
