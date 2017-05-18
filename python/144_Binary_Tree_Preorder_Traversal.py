class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
       
class Solution(object):
    def inorder(self, root):
        if not root: return []
        ans, stack = [], [root]
        while stack:
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans
        
