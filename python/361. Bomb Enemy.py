"""
361. Bomb Enemy
Medium

Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E' or empty '0', return the maximum enemies you can kill using one bomb. You can only place the bomb in an empty cell.

The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.

Example 1:
Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3

Example 2:
Input: grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
Output: 1
"""


"""
The brute force solution is very intuitive.. just count 'E's in rows and cols for each 0 in the matrix and return the maximum. This takes O((MN)*(M+N)) as you have to traverse up, down, left, and right for every i,j.

We can optimize on this by doing 4 passes and adding the number of E's seen so far, and reset if we see a 'W'.
From left to right then right to left for E's seen in each row. And then from up to down and down to up for each E seen so far in column.

Total time -> O(4*MN) --> O(MN)

"""


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[0 for _ in range(N)] for _ in range(M)]

        # left->right
        for i in range(M):
            cur = 0
            for j in range(N):
                if grid[i][j] == 'W':
                    cur = 0
                if grid[i][j] == 'E':
                    cur += 1
                else:
                    dp[i][j] = cur
        # right->left
        for i in range(M):
            cur = 0
            for j in range(N-1, -1, -1):
                if grid[i][j] == 'W':
                    cur = 0
                if grid[i][j] == 'E':
                    cur += 1
                else:
                    dp[i][j] += cur
        # up->down
        for j in range(N):
            cur = 0
            for i in range(M):
                if grid[i][j] == 'W':
                    cur = 0
                if grid[i][j] == 'E':
                    cur += 1
                else:
                    dp[i][j] += cur
        # down->up
        for j in range(N):
            cur = 0
            for i in range(M-1, -1, -1):
                if grid[i][j] == 'W':
                    cur = 0
                if grid[i][j] == 'E':
                    cur += 1
                else:
                    dp[i][j] += cur

        return max(dp[i][j] for i in range(M) for j in range(N))
