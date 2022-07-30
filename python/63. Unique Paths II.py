"""
63. Unique Paths II
Medium

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1"""


"""
Algorithm:
Define fn(i, j) as number of unique paths arriving at i, j. Then,

fn(i, j) = fn(i-1, j) + fn(i, j-1) except for fn(i, j) = 0 if obstacleGrid[i][j] == 1
"""


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        """
        Time complexity O(MN)
        Space complexity O(MN)
        """
        M, N = len(grid), len(grid[0])  # dimensions

        @lru_cache(None)
        def arriveAt(i, j):
            """Return number of unique paths arriving at (i, j)."""
            if grid[i][j] or i < 0 or j < 0:
                return 0
            if i == j == 0:
                return 1
            return arriveAt(i-1, j) + arriveAt(i, j-1)

        return arriveAt(M-1, N-1)


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [0] * N
        dp[0] = 1
        for i, j in product(range(M), range(N)):
            if grid[i][j]:
                dp[j] = 0
            elif j:
                dp[j] += dp[j-1]
        return dp[-1]
