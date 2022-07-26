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


import collections


class Solution(object):
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        BFS search, maintain a queue of (i, j, path) and a set of visited (i,j)
        When inbound and not visited and grid[p][q]==0, add neighbors to the queue
        When adding a neighbor, path += 1, queue.append((p, q, path + 1))
        When (i,j) == (M,N), return path
        """
        if not grid or not grid[0] or (grid[0][0] + grid[-1][-1]) > 0:
            return -1

        visited = set((0, 0))
        queue = collections.deque([(0, 0, 1)])
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1),
                     (1, 1), (-1, -1), (1, -1), (-1, 1)]
        M, N = len(grid), len(grid[0])

        while queue:
            i, j, path = queue.popleft()
            if (i, j) == (M-1, N-1):
                return path

            for dx, dy in neighbors:
                p, q = i+dx, j+dy
                isInbound = 0 <= p < M and 0 <= q < N
                notVisited = (p, q) not in visited
                if isInbound and notVisited and grid[p][q] == 0:
                    visited.add((p, q))
                    queue.append((p, q, path + 1))

        return -1
