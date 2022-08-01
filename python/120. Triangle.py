"""
120. Triangle
Medium

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10
"""

top-down(time complexity O(N ^ 2) | space complexity O(N ^ 2))


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Top-down DP
        time: O(N ^ 2), space: O(N ^ 2)
        """
        @lru_cache(None)
        def minPath(i, j):
            """Return min path sum ending at (i, j)"""
            if i < 0:
                return 0
            if j < 0 or j > i:
                return inf
            return triangle[i][j] + min(minPath(i-1, j-1), minPath(i-1, j))

        N = len(triangle)
        return min(minPath(N-1, j) for j in range(N+1))


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Bottom-up DP
        time: O(N ^ 2), space: O(N ^ 2)
        """
        dp = [0] * len(triangle)
        for i, row in enumerate(triangle):
            for j in reversed(range(len(row))):
                if j == 0:
                    dp[j] += row[j]
                elif j == len(triangle[i])-1:
                    dp[j] = dp[j-1] + row[j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + row[j]
        return min(dp)


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in reversed(range(len(triangle)-1)):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i-1][max(0, j-1):j+1])
        return min(triangle[-1])
