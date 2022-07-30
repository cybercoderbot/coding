"""
286. Walls and Gates
Medium

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle. 0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example 1:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Example 2:
Input: rooms = [[-1]]
Output: [[-1]]
"""


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Starting from gates, BFS traverse the grid and fill in distance to nearest gates.
        Time: O(M * N), Space: O(M * N)
        """

        M, N = len(rooms), len(rooms[0])
        MAX = 2**31 - 1
        queue = [(i, j)
                 for i, j in product(range(M), range(N)) if rooms[i][j] == 0]

        dist = 0
        while queue:
            dist += 1
            queue2 = []
            for i, j in queue:
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                    if 0 <= ii < M and 0 <= jj < N and rooms[ii][jj] == MAX:
                        rooms[ii][jj] = dist
                        queue2.append((ii, jj))
            queue = queue2

        return


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:

        if not rooms:
            return

        nrow, ncol = len(rooms), len(rooms[0])

        for i in range(nrow):
            for j in range(ncol):
                if rooms[i][j] == 0:
                    # self.dfs(rooms, i, j, 0)
                    self.dfs(rooms, i+1, j, 1)
                    self.dfs(rooms, i-1, j, 1)
                    self.dfs(rooms, i, j+1, 1)
                    self.dfs(rooms, i, j-1, 1)

    def dfs(self, rooms, i, j, val):
        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]):
            return
        if rooms[i][j] > val:
            rooms[i][j] = val
            self.dfs(rooms, i+1, j, val+1)
            self.dfs(rooms, i-1, j, val+1)
            self.dfs(rooms, i, j+1, val+1)
            self.dfs(rooms, i, j-1, val+1)
