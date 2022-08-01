"""
85. Maximal Rectangle
Hard

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1
"""


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Use DP to keep track of low and high of given max height at given point.
        Bottom-up DP
        Time: O(M * N), Space: O(N)
        """
        if not matrix:
            return 0

        res = 0
        M, N = len(matrix), len(matrix[0])
        height, low, high = [0]*N, [0]*N, [N]*N
        for i in range(M):
            left, right = 0, N
            for j in range(N):
                if matrix[i][j] == "1":
                    height[j] += 1
                    low[j] = max(low[j], left)
                else:
                    height[j] = low[j] = 0
                    left = j+1
                if matrix[i][-(j+1)] == "1":
                    high[-(j+1)] = min(high[-(j+1)], right)
                else:
                    high[-(j+1)] = N
                    right = N-j-1

            area = max((x2-x1)*h for x2, x1, h in zip(high, low, height))
            res = max(res, area)

        return res


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Top-down implementation
        """
        if not matrix:
            return 0

        M, N = len(matrix), len(matrix[0])

        @lru_cache(None)
        def height(i, j):
            if i < 0 or matrix[i][j] == "0":
                return 0
            return height(i-1, j) + 1

        @lru_cache(None)
        def left(i, j):
            if j == -1 or matrix[i][j] == "0":
                return j+1
            return left(i, j-1)

        @lru_cache(None)
        def low(i, j):
            if i < 0 or matrix[i][j] == "0":
                return 0
            return max(low(i-1, j), left(i, j))

        @lru_cache(None)
        def right(i, j):
            if j == N or matrix[i][j] == "0":
                return j
            return right(i, j+1)

        @lru_cache(None)
        def high(i, j):
            if i < 0 or matrix[i][j] == "0":
                return N
            return min(high(i-1, j), right(i, j))

        @lru_cache(None)
        def area(i, j):
            return height(i, j) * (high(i, j) - low(i, j))

        return max(area(i, j) for i, j in product(range(M), range(N)))
