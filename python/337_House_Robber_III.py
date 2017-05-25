# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        #         4
        #        /
        #       1
        #      /
        #     2
        #    /
        #   3


        # 如果隔一个偷，那么是4+2=6，其实最优解应为4+3=7，隔了两个，所以说纯粹是怎么多怎么来，
        # 那么这种问题是很典型的递归问题，我们可以利用Back-tracking来做，因为当前的计算需要依赖之前的结果，
        # 那么我们对于某一个节点，如果其左子节点存在，我们通过递归调用函数，算出不包含左子节点返回的值，
        # 同理，如果右子节点存在，算出不包含右子节点返回的值，那么此节点的最大值可能有两种情况，一种是
        # 该节点值加上不包含左子节点和右子节点的返回值之和，另一种是左右子节点返回值之和不包含当期节点值，
        # 取两者的较大值返回即可
        
        # 上面的方法重复计算了很多地方，比如要完成一个节点的计算，就得一直找左右子节点计算，
        # 我们可以把已经算过的节点用哈希表保存起来，以后递归调用的时候，现在哈希表里找，
        # 如果存在直接返回，如果不存在，等计算出来后，保存到哈希表中再返回，这样方便以后再调用
        
        
        visited = {}
        return self.dfs(root, visited)
        
    def dfs(self, root, visited):
        if not root: return 0
        if root in visited: return visited[root];
        val = 0
        if root.left:
            val += self.dfs(root.left.left, visited) + self.dfs(root.left.right, visited)
        if root.right:
            val += self.dfs(root.right.left, visited) + self.dfs(root.right.right, visited)
        val = max(val + root.val, self.dfs(root.left, visited) + self.dfs(root.right, visited))
        visited[root] = val
        return val
        
        
        
