# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # 这道题给定了一棵完全二叉树，让我们求其节点的个数。让我们来看看维基百科上对二者的定义：

        # 完全二叉树：对于一颗二叉树，假设其深度为d（d>1）。除了第d层外，其它各层的节点数目均已达最大值，
        # 且第d层所有节点从左向右连续地紧密排列，这样的二叉树被称为完全二叉树
        
        # 满二叉树：对于上述的完全二叉树，如果去掉其第d层的所有节点，那么剩下的部分就构成一个满二叉树
        # （此时该满二叉树的深度为d-1）

        # 通过上面的定义，我们可以看出二者的关系是，满二叉树一定是完全二叉树，
        # 而完全二叉树不一定是满二叉树。那么这道题给的完全二叉树就有可能是满二叉树，若是满二叉树，节点个数很好求，
        # 为2的h次方-1，h为该满二叉树的高度。这道题可以用递归和非递归两种方法来解。我们先来看递归的方法，思路是
        # 分别找出以当前节点为根节点的左子树和右子树的高度并对比，如果相等，则说明是满二叉树，直接返回节点个数，
        # 如果不相等，则节点个数为左子树的节点个数加上右子树的节点个数再加1(根节点)，其中左右子树节点个数的计算
        # 可以使用递归来计算

        if not root:
            return 0
            
        hleft = hright = 0
        pleft = pright = root
        
        while pleft:
            hleft += 1
            pleft = pleft.left
        
        while pright:
            hright += 1
            pright = pright.right
        
        if hleft==hright:
            return pow(2, hleft)-1
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        
        
        
        
