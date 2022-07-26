import math


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        这道题给我们了一些建筑物的坐标和一些障碍物的坐标，让我们找一个位置，使其到所有建筑物的曼哈顿距离之和最小，
        这道题有了障碍物的存在，这样就使得直接使用曼哈顿距离的计算公式变得不可行，因为在有些情况下，障碍物完全封死
        了某个建筑物，那么这时候应该返回-1。所以这道题只能使用遍历迷宫的思想来解，那么这题就和之前那道Walls and Gates
        很类似，但是这道题用DFS就会很麻烦，因为我们的目标是要建立Distance Map，所以BFS的特性使得其非常适合建立距离场，
        而DFS由于是沿着一个方向一股脑的搜索，然后之后会面临着更新距离的问题，那么只有当递归函数都调用结束后，距离场才
        建立好，那么我们累加距离场时又得整个遍历一遍，非常不高效。主要原因还是由于DFS的搜索方式不适合距离场，因为BFS
        遍历完一个点后，不会再来更改这个点的值，而DFS会反复的更改同一个点的值，所以这道题还是老老实实地用BFS来解题吧，
        还是需要借助queue来遍历，我们对于每一个建筑的位置都进行一次全图的BFS遍历，每次都建立一个dist的距离场，由于我们
        BFS遍历需要标记应经访问过的位置，而我们并不想建立一个visit的二维矩阵，那么怎么办呢，这里用一个小trick，我们第一
        遍历的时候，都是找0的位置，遍历完后，我们将其赋为-1，这样下一轮遍历我们就找-1的位置，然后将其都赋为-2，
        以此类推直至遍历完所有的建筑物，然后在遍历的过程中更新dist和sum的值，并且更新结果res的值，最后根据res的值看是否
        要返回-1

        # Use hit to record how many times a 0 grid has been reached and use distSum to record
        # the sum of distance from all 1 grids to this 0 grid. A powerful pruning is that during
        # the BFS we count how many 1 grids we reached. If count < total, then we know not all 1
        # grids are connected are we can return -1 immediately, which greatly improved speed.

        if not grid or not grid[0]:
            return -1
        r, c = len(grid), len(grid[0])

        total = sum(x for row in grid for x in row if x == 1)
        hit = [[0]*c for _ in range(r)]
        dist = [[0]*c for _ in range(r)]

        def bfs(x, y):
            visited = set()
            visited.add((x, y))
            count = 1
            q = [(x, y, 0)]
            while q:
                x, y, d = q.pop(0)
                for (i, j) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if i < 0 or i >= r or j < 0 or j >= c or (i, j) in visited:
                        continue
                    visited.add((i, j))
                    if grid[i][j] == 0:
                        q.append((i, j, d+1))
                        hit[i][j] += 1
                        dist[i][j] += (d+1)
                    elif grid[i][j] == 1:
                        count += 1
            return count == total

        for x in range(r):
            for y in range(c):
                if grid[x][y] == 1:
                    if not bfs(x, y):
                        return -1

        ans = float("inf")
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0 and hit[i][j] == total:
                    ans = min(dist[i][j], ans)

        if ans == float("inf"):
            return -1
        else:
            return ans
