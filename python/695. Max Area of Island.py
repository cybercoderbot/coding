"""
695. Max Area of Island
Medium

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 
Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.


Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0]) 
        
        def dfs(x, y): 
            """Return island area."""
            area = 1
            grid[x][y] = 0 # mark as visited 
            for i, j in (x-1, y), (x, y-1), (x, y+1), (x+1, y):
                if 0 <= i < M and 0 <= j < N and grid[i][j]: 
                    area += dfs(i, j)
            return area 
        
        res = 0
        for x in range(M):
            for y in range(N): 
                if grid[x][y]: 
                    res = max(res, dfs(x, y))
        return res 
    
    
    
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        res = 0
        for r in range(M):
            for c in range(N): 
                if grid[r][c]: 
                    area = 1
                    grid[r][c] = 0
                    stack = [(r, c)]
                    while stack: 
                        x, y = stack.pop()
                        neighbors = [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]
                        for i, j in neighbors:
                            if 0 <= i < M and 0 <= j < N and grid[i][j]: 
                                area += 1
                                grid[i][j] = 0 
                                stack.append((i, j))
                    res = max(res, area)
        return res 
        