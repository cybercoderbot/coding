"""
317. Shortest Distance from All Buildings
Hard

You are given an m x n grid grid of values 0, 1, or 2, where:
each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example 1:
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.

Example 2:
Input: grid = [[1,0]]
Output: 1

Example 3:
Input: grid = [[1]]
Output: -1
"""


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        @lru_cache(None)
        def bfs(i, j, count):
            queue = collections.deque([(i, j, 0)])
            while queue:
                i0, j0, step = queue.popleft()
                for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
                    i, j = i0 + di, j0 + dj
                    # only the position be visited by count times will be appended to queue
                    if 0 <= i < M and 0 <= j < N and visited[i][j][1] == count and not grid[i][j]:
                        visited[i][j][0] += step+1
                        visited[i][j][1] = count+1
                        queue.append((i, j, step+1))
            return

        M, N = len(grid), len(grid[0])
        visited = [[[0, 0] for i in range(N)] for j in range(M)]

        count = 0    # number of building we have visited
        for i, j in product(range(M), range(N)):
            if grid[i][j] == 1:
                bfs(i, j, count)
                count += 1

        res = inf
        for i, j in product(range(M), range(N)):
            if visited[i][j][1] == count:
                res = min(res, visited[i][j][0])

        return res if res != inf else -1
