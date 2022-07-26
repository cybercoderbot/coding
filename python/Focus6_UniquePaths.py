"""
62. Unique Paths
Medium

9984

316

Add to List

Share
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""


"""
Approach 1 - dynamic programming
The recursion is dp[i, j] = dp[i-1,j] + dp[i,j-1], with boundary condition 
dp[0,j] = dp[i,0] = 1.
"""




from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Time complexity O(MN)
        Space complexity O(MN)
        """

        @lru_cache(None)
        def dp(i, j):
            if not (i and j):
                return 1
            return dp(i-1, j) + dp(i, j-1)

        return dp(m-1, n-1)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        I was in fact once asked by an interviewer how to avoid defining memo outside of the function. Here is one implementation with memo in argument 
        """

        def fn(i, j, memo={}):
            if (i, j) in memo:
                return memo[i, j]

            if i * j == 0:
                memo[i, j] = 1
            else:
                memo[i, j] = fn(i-1, j, memo) + fn(i, j-1, memo)

            return memo[i, j]

        return fn(m-1, n-1)


"""
There are in total m+n-2 moves in which m-1 is to the bottom and n-1 is to the right. 
As a result, there are m+n-2 choose m-1 total paths.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        The bottom-up implementation could reduce space usage to O(M) (or even better O(min(M, N)).

        Time complexity O(MN)
        Space complexity O(M)

        """
        dp = [1]*n
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i-1]
        return dp[-1]


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
        m, n = len(grid), len(grid[0])  # dimensions

        @cache
        def fn(i, j):
            """Return number of unique paths arriving at (i, j)."""
            if grid[i][j] or i < 0 or j < 0:
                return 0
            if i * j == 0:
                return 1
            return fn(i-1, j) + fn(i, j-1)

        return fn(m-1, n-1)


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0]*n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dp[j] = 0
                elif j:
                    dp[j] += dp[j-1]
        return dp[-1]


"""
980. Unique Paths III
Hard

You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)


Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)


Example 3:
Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
"""


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        empty = 0
        for i, j in product(range(M), range(N)):
            if grid[i][j] == 1:
                x0, y0 = i, j
            elif grid[i][j] == 0:
                empty += 1  # empty squares

        def backtrack(i, j, empty):
            """Count paths via backtracking."""
            nonlocal res
            if grid[i][j] == 2:
                if empty == -1:
                    res += 1
                return

            grid[i][j] = -1  # mark as visited
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                if 0 <= ii < M and 0 <= jj < N and grid[ii][jj] != -1:
                    backtrack(ii, jj, empty-1)
            grid[i][j] = 0  # backtracking

            return

        res = 0
        backtrack(x0, y0, empty)
        return res
