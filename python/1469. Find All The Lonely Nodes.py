"""
1469. Find All The Lonely Nodes
Easy

In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.

Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.

Example 1:
Input: root = [1,2,3,null,4]
Output: [4]
Explanation: Light blue node is the only lonely node.
Node 1 is the root and is not lonely.
Nodes 2 and 3 have the same parent and are not lonely.

Example 2:
Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2]
Output: [6,2]
Explanation: Light blue nodes are lonely nodes.
Please remember that order doesn't matter, [2,6] is also an acceptable answer.

Example 3:
Input: root = [11,99,88,77,null,null,66,55,null,null,44,33,null,null,22]
Output: [77,55,33,66,44,22]
Explanation: Nodes 99 and 88 share the same parent. Node 11 is the root.
All other nodes are lonely.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    @lru_cache(None)
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if root.left and not root.right:
            return [root.left.val] + self.getLonelyNodes(root.left)
        if not root.left and root.right:
            return [root.right.val] + self.getLonelyNodes(root.right)
        return self.getLonelyNodes(root.left) + self.getLonelyNodes(root.right)


class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        res = []

        @lru_cache(None)
        def dfs(node):
            if node.left and not node.right:
                res.append(node.left.val)

            if node.right and not node.left:
                res.append(node.right.val)

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        return res


class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        """
        Iterative preorder DFS solution
        Traverse the tree depth-first in preorder and collect lonely nodes.
        1) not node.right -> res.append(node.left.val)
        2) not node.left  -> res.append(node.right.val)
        Time: O(N), Space: O(N)
        """
        res = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                if not node.right:
                    res.append(node.left.val)
            if node.right:
                queue.append(node.right)
                if not node.left:
                    res.append(node.right.val)
        return res
