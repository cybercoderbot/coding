"""
742. Closest Leaf in a Binary Tree
Medium

Given the root of a binary tree where every node has a unique value and a target integer k, return the value of the nearest leaf node to the target k in the tree.

Nearest to a leaf means the least number of edges traveled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

Example 1:
Input: root = [1,3,2], k = 1
Output: 2
Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.

Example 2:
Input: root = [1], k = 1
Output: 1
Explanation: The nearest leaf node is the root node itself.

Example 3:
Input: root = [1,2,3,4,null,null,null,5,null,6], k = 2
Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
 
Constraints:

The number of nodes in the tree is in the range [1, 1000].
1 <= Node.val <= 1000
All the values of the tree are unique.
There exist some node in the tree where Node.val == k.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        parent = {root: None}
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == k:
                src = node
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        queue = deque([src])
        seen = {src}
        while queue:
            node = queue.popleft()
            if not node.left and not node.right:
                return node.val
            for p in (node.left, node.right, parent[node]):
                if p and p not in seen:
                    queue.append(p)
                    seen.add(p)
