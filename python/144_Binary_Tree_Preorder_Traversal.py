class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorder(self, root):
         """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        ans, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                # add node.val before going to all children
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans
        
