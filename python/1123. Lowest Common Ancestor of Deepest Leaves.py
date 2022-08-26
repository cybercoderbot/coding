"""
1123. Lowest Common Ancestor of ALL Deepest Leaves
"""


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        parent = {}
        queue = collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node)
                if node.left:
                    queue.append(node.left)
                    parent[node.left] = node
                if node.right:
                    queue.append(node.right)
                    parent[node.right] = node

        while len(level) > 1:
            ancestors = set()
            for node in level:
                ancestors.add(parent[node])
            level = list(ancestors)

        return level[0]
