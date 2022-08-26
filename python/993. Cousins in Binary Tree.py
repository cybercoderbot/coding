"""
993. Cousins in Binary Tree
Easy

Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
"""


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        Preorder DFS iteration
        Traverse the tree and collect depth and parent for the node with value x and y.

        stack: (node, depth, parent)
        res[node] = (depth, parent)
        """
        res = defaultdict(tuple)
        queue = collections.deque([(root, 0, None)])
        while queue:
            node, depth, parent = queue.popleft()
            if not node:
                continue
            if node.val in (x, y):
                res[node.val] = (depth, parent)
            queue.append((node.left, depth+1, node))
            queue.append((node.right, depth+1, node))

        depth1, parent1 = res[x]
        depth2, parent2 = res[y]

        return depth1 == depth2 and parent1 != parent2


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        Preorder DFS recursion
        """

        def dfs(node, depth, parent):
            """Traverse the subtree rooted at node"""
            if node is None:
                return
            if node.val in (x, y):
                res[node.val] = (depth, parent)

            dfs(node.left, depth+1, node)
            dfs(node.right, depth+1, node)

            return

        res = defaultdict(tuple)
        dfs(node=root, depth=0, parent=None)

        depth1, parent1 = res[x]
        depth2, parent2 = res[y]

        return depth1 == depth2 and parent1 != parent2


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """
        BFS search
        """
        queue = [(root, None)]

        while queue:
            level = []
            seen = False
            for node, parent in queue:
                if node.val in (x, y):
                    if not seen:
                        seen = parent
                    else:
                        return seen != parent
                if node.left:
                    level.append((node.left, node))
                if node.right:
                    level.append((node.right, node))
            if seen:
                return False

            queue = level
