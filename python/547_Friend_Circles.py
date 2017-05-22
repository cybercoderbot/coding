class Solution(object):

    
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        # 这道题让我们求朋友圈的个数，题目中对于朋友圈的定义是可以传递的，比如A和B是好友，B和C是好友，
        # 那么即使A和C不是好友，那么他们三人也属于一个朋友圈。那么比较直接的解法就是DFS搜索，对于某个人，
        # 遍历其好友，然后再遍历其好友的好友，那么我们就能把属于同一个朋友圈的人都遍历一遍，我们同时标记出
        # 已经遍历过的人，然后累积朋友圈的个数，再去对于没有遍历到的人在找其朋友圈的人，这样就能求出个数。
        # 其实这道题的本质是之前那道题Number of Connected Components in an Undirected Graph，
        # 其实许多题目的本质都是一样的，就是看我们有没有一双慧眼能把它们识别出来.
        
        
        n = len(M)
        if n<2: return n
        
        visited = set()
        
        def dfs(i):
            for x in range(n):
                if M[i][x] and x not in visited:
                    visited.add(x)
                    dfs(x)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
        
        
