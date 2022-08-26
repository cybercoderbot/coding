class Solution:
    def uniquePaths(self, M: int, N: int) -> int:
        """
        62. Unique Paths
        """
        @lru_cache(None)
        def arrive(i, j):
            if not i or not j:
                return 1
            return arrive(i-1, j) + arrive(i, j-1)

        return arrive(M-1, N-1)


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        """
        63. Unique Paths II (obstacle: 1)
        Time O(M * N), Space O(M * N)
        """
        M, N = len(grid), len(grid[0])

        @lru_cache(None)
        def arrive(i, j):
            """Return number of unique paths arriving at (i, j)."""
            if grid[i][j] or i < 0 or j < 0:
                return 0
            if i == j == 0:
                return 1
            return arrive(i-1, j) + arrive(i, j-1)

        return arrive(M-1, N-1)


class Solution:
    def findPaths(grid: List[List[int]]) -> List[List[int]]:
        """
        grid = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
        paths:
            [1, 4, 7, 8, 9]
            [1, 4, 5, 8, 9]
            [1, 4, 5, 6, 9]
            [1, 2, 5, 8, 9]
            [1, 2, 5, 6, 9]
            [1, 2, 3, 6, 9]
        """
        if not grid or not grid[0]:
            return

        def find(path, i, j):
            """Find path ending at (i,j)"""
            path.append(grid[i][j])
            if i == M-1 and j == N-1:
                res.append(path)
                return
            if i+1 < M:
                find(path, i+1, j)
            if j+1 < N:
                find(path, i, j+1)
            # backtrack
            path.pop()
            return

        res = []
        M, N = len(grid), len(grid[0])
        find(path=[], i=0, j=0)
        return res


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
        Unique Paths III
        Return the number of 4-directional walks from the starting square to
        the ending square, that walk over every non-obstacle square exactly once.
        """
        M, N = len(grid), len(grid[0])  # dimensions
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
            # backtrack
            grid[i][j] = 0
            return

        res = 0
        backtrack(x0, y0, empty)
        return res


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        695. Max Area of Island
        BFS from all non-zero nodes. Keep track of max area.
        """
        if not grid:
            return 0

        res = 0
        M, N = len(grid), len(grid[0])
        for i, j in product(range(M), range(N)):
            if not grid[i][j]:
                continue
            area = 1
            grid[i][j] = 0
            queue = collections.deque([(i, j)])
            while queue:
                i, j = queue.popleft()
                for x, y in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                    if 0 <= x < M and 0 <= y < N and grid[x][y]:
                        area += 1
                        grid[x][y] = 0
                        queue.append((x, y))
            res = max(res, area)
        return res
