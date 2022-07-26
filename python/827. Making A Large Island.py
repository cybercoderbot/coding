"""
827. Making A Large Island
Hard

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.


Example 2:
Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:
Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

Approach: Component Sizes
Intuition

As in the previous solution, we check every 0. However, we also store the size of each group, so that we do not have to use depth-first search to repeatedly calculate the same size.

However, this idea fails when the 0 touches the same group. For example, consider grid = [[0,1],[1,1]]. The answer is 4, not 1 + 3 + 3, since the right neighbor and the bottom neighbor of the 0 belong to the same group.

We can remedy this problem by keeping track of a group id (or index), that is unique for each group. Then, we'll only add areas of neighboring groups with different ids.

Algorithm

For each group, fill it with value index and remember it's size as area[index] = dfs(...).

Then for each 0, look at the neighboring group ids seen and add the area of those groups, plus 1 for the 0 we are toggling. This gives us a candidate answer, and we take the maximum.

To solve the issue of having potentially no 0, we take the maximum of the previously calculated areas.


Complexity Analysis

Time Complexity: O(N^2), where NN is the length and width of the grid.

Space Complexity: O(N^2), the additional space used in the depth first search by area.
"""


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        index = 2
        area = defaultdict(int)
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    stack = [(r, c)]
                    grid[r][c] = index
                    while stack:
                        x, y = stack.pop()
                        area[index] += 1
                        for i, j in (x-1, y), (x, y-1), (x, y+1), (x+1, y):
                            if 0 <= i < N and 0 <= j < N and grid[i][j] == 1:
                                stack.append((i, j))
                                grid[i][j] = index
                    index += 1

        res = max(area.values(), default=0)
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    candidate = 1
                    seen = set()
                    for i, j in (x-1, y), (x, y-1), (x, y+1), (x+1, y):
                        if 0 <= i < N and 0 <= j < N and grid[i][j] and grid[i][j] not in seen:
                            seen.add(grid[i][j])
                            candidate += area[grid[i][j]]
                    res = max(res, candidate)
        return res


class Solution(object):
    def largestIsland(self, grid):
        N = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc

        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans

        area = {}
        index = 2
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        res = max(area.values() or [0])
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc]
                            for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    res = max(res, 1 + sum(area[i] for i in seen))
        return res
