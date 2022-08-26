class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        463. Island Perimeter
        Solution 1: Scan through grid and at any position check if it is different
        from its four neighbors. Add 1 to res for one difference. Return the count
        of differences at last.
        """
        if not grid:
            return 0
        M, N = len(grid), len(grid[0])
        res = 0
        for i, j in product(range(M), range(N)):
            if not grid[i][j]:
                continue
            if i == 0 or not grid[i-1][j]:
                res += 1
            if j == 0 or not grid[i][j-1]:
                res += 1
            if i == M-1 or not grid[i+1][j]:
                res += 1
            if j == N-1 or not grid[i][j+1]:
                res += 1
        return res


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        463. Island Perimeter
        Solution 2: scan through grid, at any position, check if it is 1.
        If so, add 4 to res (4 lines in its boundary).
        Check the cell above it and to the left of it. If grid[i-1][j] == 1, then we need to subtract 2 from res since there isn't a boundary between grid[i-1][j] and grid[i][j] and yet we've added it twice at i-1, j and i, j, and the same for grid[i][j-1] and grid[i][j].
        """
        if not grid:
            return 0
        M, N = len(grid), len(grid[0])
        res = 0
        for i, j in product(range(M), range(N)):
            if not grid[i][j]:
                continue
            res += 4
            if i and grid[i-1][j]:
                res -= 2
            if j and grid[i][j-1]:
                res -= 2
        return res


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        695. Max Area of Island
        """
        if not grid:
            return 0
        M, N = len(grid), len(grid[0])

        @lru_cache(None)
        def getArea(i, j):
            area = 1
            # mark as visited
            grid[i][j] = 0
            for x, y in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                if 0 <= x < M and 0 <= y < N and grid[x][y]:
                    area += getArea(x, y)
            return area

        res = 0
        for i, j in product(range(M), range(N)):
            if grid[i][j]:
                res = max(res, getArea(i, j))
        return res


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        695. Max Area of Island
        """
        if not grid:
            return 0
        M, N = len(grid), len(grid[0])
        res = 0
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


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Iterate through each of the cell. If it is an island (1):
        1) Increase the res by 1
        2) DFS to mark all adjacent visited islands
        """
        if not grid:
            return 0

        M, N = len(grid), len(grid[0])
        res = 0
        for i, j in product(range(M), range(N)):
            if grid[i][j] == '1':
                res += 1
                self.markVisited(grid, i, j)
        return res

    def markVisited(self, grid, i, j):
        M, N = len(grid), len(grid[0])
        if 0 <= i < M and 0 <= j < N and grid[i][j] == '1':
            grid[i][j] = '#'
            self.markVisited(grid, i+1, j)
            self.markVisited(grid, i-1, j)
            self.markVisited(grid, i, j+1)
            self.markVisited(grid, i, j-1)
        return


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        976. Largest Perimeter Triangle
        Return the largest perimeter of a triangle choosing 3 sides from nums
        """
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        1905. Count Sub Islands
        Return the number of islands in grid2 that are considered sub-islands of grid1
        """
        if not grid1 or not grid2:
            return 0
        M, N = len(grid1), len(grid1[0])

        @lru_cache(None)
        def isSubIsland(i, j):
            """Return True if i, j is in a sub-island."""
            grid2[i][j] = 0  # mark as visited
            flag = grid1[i][j]
            for x, y in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                if 0 <= x < M and 0 <= y < N and grid2[x][y]:
                    flag &= isSubIsland(x, y)
            return flag

        res = 0
        for i, j in product(range(M), range(N)):
            if grid2[i][j] and isSubIsland(i, j):
                res += 1
        return res
