# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, num):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        # 这道二叉树路径之和在之前的基础上又需要找出路径, 基本思想都一样，还是需要用深度优先搜索DFS，
        # 只不过数据结构相对复杂一点，需要用到二维的list，而且每当DFS搜索到新节点时，都要保存该节点。
        # 而且每当找出一条路径之后，都将这个保存为一维list的路径保存到最终结果二维list中。并且，
        # 每当DFS搜索到子节点，发现不是路径和时，返回上一个结点时，需要把该节点从一维list中移除
        
        if not root: return []
        res = []
        self.dfs(root, num, [], res)
        return res
        
    def dfs(self, root, num, path, res):
        if not root.left and not root.right and num == root.val:
            path.append(root.val)
            res.append(path)
        if root.left:
            self.dfs(root.left, num-root.val, path+[root.val], res)
        if root.right:
            self.dfs(root.right, num-root.val, path+[root.val], res)
        
        
        
        
        
