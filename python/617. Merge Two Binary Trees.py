"""
617. Merge Two Binary Trees
Easy

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

 

Example 1:

Example 1:
Input: 
  Tree 1                     Tree 2                  
          1                         2                             
         / \\                       / \\                            
        3   2                     1   3                        
      /                           \\   \\                      
      5                             4   7                  
Output: 
Merged tree:
       3
      / \
     4   5
    / \\   \\ 
   5   4   7

Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not t1 or not t2:
            return t1 or t2

        merged = TreeNode(t1.val + t2.val)
        merged.left = self.mergeTrees(t1.left, t2.left)
        merged.right = self.mergeTrees(t1.right, t2.right)

        return merged
