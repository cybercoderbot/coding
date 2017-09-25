#  Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its 
# elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return 
# the new root of the trimmed binary search tree.

# Example 1:

# Input: 
#     1
#    / \
#   0   2

#   L = 1
#   R = 2

# Output: 
#     1
#       \
#        2

# Example 2:

# Input: 
#     3
#    / \
#   0   4
#    \
#     2
#    /
#   1

#   L = 1
#   R = 3

# Output: 
#       3
#      / 
#    2   
#   /
#  1

# 对于二叉树的题，十有八九都是要用递归来解的。首先判断如果root为空，那么直接返回空即可。然后就是要看根结点是否在范围内，
# 如果根结点值小于L，那么返回对其右子结点调用递归函数的值；如果根结点大于R，那么返回对其左子结点调用递归函数的值。
# 若根结点在范围内，将其左子结点更新为对其左子结点调用递归函数的返回值，同样，将其右子结点更新为对其右子结点调用递归函数的返回值。最后返回root。


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root
        
        
        
        
