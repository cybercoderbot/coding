class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # Walk through the matrix. At the start of each non-wall-streak (row-wise or column-wise),
        # count the number of hits in that streak and remember it. O(mn) time, O(n) space.

        # 这种解法需要一个row_hit变量，用来记录到下一个墙之前的敌人个数。还需要一个数组col_hits，其中
        # col_hits[j]表示第j列到下一个墙之前的敌人个数。算法思路是遍历整个数组grid，对于位置grid[i][j]，
        # 对于水平方向，如果当前位置是开头或者前一个是墙壁，我们开始从当前位置往后遍历，遍历到末尾或者
        # 墙的位置停止，计算敌人个数。对于竖直方向也是同样，如果当前位置是开头或者上一个是墙壁，我们开始
        # 从当前位置向下遍历，遍历到末尾或者墙的位置停止，计算敌人个数。有了水平方向和竖直方向敌人的个数，
        # 那么如果当前位置是0，表示可以放炸弹，我们更新结果ans即可

        if not grid:
            return 0
        ht, wd = len(grid), len(grid[0])
        ans = 0
        col_hits = [0] * wd
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if j == 0 or row[j-1] == 'W':
                    row_hit = 0
                    k = j
                    while k < wd and row[k] != 'W':
                        row_hit += row[k] == 'E'
                        k += 1
                if i == 0 or grid[i-1][j] == 'W':
                    col_hits[j] = 0
                    k = i
                    while k < ht and grid[k][j] != 'W':
                        col_hits[j] += grid[k][j] == 'E'
                        k += 1
                if cell == '0':
                    ans = max(ans, row_hit + col_hits[j])
        return ans
