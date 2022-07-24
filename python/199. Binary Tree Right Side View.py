"""
199. Binary Tree Right Side View
Medium

7874

457

Add to List

Share
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


Solution
Traverse the tree and put the rightmost node of each level to a container.



"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
# recursive preorder dfs
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        def traverse(node, i): 
            """Traverse the tree depth-first"""
            if not node: 
                return 
            if i == len(res): 
                res.append(node.val)
                
            traverse(node.right, i+1)
            traverse(node.left, i+1)
            
        res = []
        traverse(root, 0)
        return res 


# iterative preorder dfs
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        stack = [(root, 0)]
        while stack:
            node, i = stack.pop()
            if node: 
                if i == len(res): 
                    res.append(node.val)
                stack.append((node.left, i+1))
                stack.append((node.right, i+1))
        return res 


# bfs
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root: 
            return []
        
        res = []
        queue1 = [root]
        while queue1: 
            qnext = []
            for node in queue1: 
                # Add child nodes of the current level for the next level
                if node.left: 
                    queue2.append(node.left)
                if node.right: 
                    queue2.append(node.right)

            # The current level is finished.
            # The last element is the rightmost one.
            res.append(node.val)

            # go to next level
            queue1 = queue2

        return res 

