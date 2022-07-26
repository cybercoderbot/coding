class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # 这道求岛屿数量的题的本质是求矩阵中连续区域的个数，很容易想到需要用深度优先搜索DFS来解，
        # 对于一个为‘1’且未被访问过的位置，我们递归进入其上下左右位置上为‘1’的数，并将其grid对应值赋为
        # v (visited)，继续进入其所有相连的邻位置，这样可以将这个连通区域所有的数找出来，并将其对应的
        # grid中的值赋v，找完次区域后，我们将结果count自增1，然后我们在继续找下一个为‘1’且未被访问过的位置，
        # 以此类推直至遍历完整个原数组即可得到最终结果

        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = 'v'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
