"""
1091. Shortest Path in Binary Matrix
Medium

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        BFS and set the visited grid as non-empty to avoid revisiting
        """
        if grid[0][0] or grid[-1][-1]:
            return -1

        N = len(grid)
        queue = [(0, 0, 1)]
        grid[0][0] = 1
        for i, j, path in queue:
            if i == j == N-1:
                return path
            nbrs = ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1),
                    (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1))
            for x, y in nbrs:
                if 0 <= x < N and 0 <= y < N and not grid[x][y]:
                    grid[x][y] = '#'
                    queue.append((x, y, path+1))
        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or (grid[0][0] + grid[-1][-1]) > 0:
            return -1

        visited = set((0, 0))
        queue = [(0, 0, 1)]
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1),
                     (1, 1), (-1, -1), (1, -1), (-1, 1)]
        M, N = len(grid), len(grid[0])

        while queue:
            x, y, path = queue.pop(0)
            if (x, y) == (M-1, N-1):
                return path

            for dx, dy in neighbors:
                p, q = x+dx, y+dy
                isInbound = 0 <= p < M and 0 <= q < N
                notVisited = (p, q) not in visited
                if isInbound and notVisited and not grid[p][q]:
                    visited.add((p, q))
                    queue.append((p, q, path + 1))

        return -1
