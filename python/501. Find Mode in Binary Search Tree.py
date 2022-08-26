"""
501. Find Mode in Binary Search Tree
Easy

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
 
Example 1:
Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        if not root:
            return

        queue = collections.deque([root])
        freq = defaultdict(int)
        while queue:
            node = queue.popleft()
            freq[node.val] += 1
            if node.left:
                queue.append((node.left))
            if node.right:
                queue.append((node.right))

        mode = max(freq.values())
        return [key for key, val in freq.items() if val == mode]
