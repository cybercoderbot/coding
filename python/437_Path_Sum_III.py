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
        :rtype: int
        """
        
        # 解题思路：Pre-order Tree Traverse
        # 这道题让我们求二叉树的路径的和等于一个给定值，说明了这条路径不必要从根节点开始，
        # 可以是中间的任意一段，而且二叉树的节点值也是有正有负。那么我们可以用递归来做，
        # 相当于先序遍历二叉树，对于每一个节点都有记录了一条从根节点到当前节点到路径
        # 在遍历节点的同时，以经过的节点为根，寻找子树中和为num的路径
        
        def preorder_traverse(root, val):
            if not root: return 0
            res = (root.val==val)
            res += preorder_traverse(root.left, val-root.val)
            res += preorder_traverse(root.right, val-root.val)
            return res
            
        if not root: return 0
        ans = preorder_traverse(root, num)
        ans += self.pathSum(root.left, num)
        ans += self.pathSum(root.right, num)
        return ans
        
        
        
        
        
