class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        
        # 这道题类似一种迷宫问题，规定了-1表示墙，0表示门，让求每个点到门的最近的曼哈顿距离，
        # 这其实类似于求距离场Distance Map的问题，那么我们先考虑用DFS来解，思路是，
        # 我们搜索0的位置，每找到一个0，以其周围四个相邻点为起点，开始DFS遍历，并带入深度值1，
        # 如果遇到的值大于当前深度值，我们将位置值赋为当前深度值，并对当前点的四个相邻点开始
        # DFS遍历，注意此时深度值需要加1，这样遍历完成后，所有的位置就被正确地更新了
        
        
        if not rooms: return 
        
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
        if i<0 or i>=len(rooms) or j<0 or j>=len(rooms[0]):
            return
        if rooms[i][j]>val:
            rooms[i][j] = val
            self.dfs(rooms, i+1, j, val+1)
            self.dfs(rooms, i-1, j, val+1)
            self.dfs(rooms, i, j+1, val+1)
            self.dfs(rooms, i, j-1, val+1)
            
            
            
            
