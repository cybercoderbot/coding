# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # And an iterative version using my own stack
        
        # 这道题让我们翻转二叉树，是树的基本操作之一，可以用递归和非递归两种方法来解。
        # 非递归的方法也不复杂，跟二叉树的层序遍历一样，需要用queue来辅助，先把根节点排入队列中，
        # 然后从队中取出来，交换其左右节点，如果存在则分别将左右节点在排入队列中，以此类推直到队列
        # 中木有节点了停止循环，返回root即可
        
        if not root: 
            return 
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        
        
        # 非递归的方法，跟二叉树的层序遍历一样，需要用queue来辅助，先把根节点排入队列中，
        # 然后从队中取出来，交换其左右节点，如果存在则分别将左右节点在排入队列中，以此类推直到队列中
        # 木有节点了停止循环，返回root即可
        
        
        row = [root]
        while row:
            node = row.pop()
            if node:
                node.left, node.right = node.right, node.left
                row.extend([node.left, node.right])
        return root
            
