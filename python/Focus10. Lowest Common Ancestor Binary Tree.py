class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        160. Intersection of Two Linked Lists
        """
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        235. Lowest Common Ancestor of a Binary Search Tree
        """
        if p.val > q.val:
            p, q = q, p

        node = root
        while node:
            if node.val < p.val:
                node = node.right
            elif p.val <= node.val <= q.val:
                return node
            else:
                node = node.left


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        236. Lowest Common Ancestor of a Binary Tree
        """
        if not root or root in (p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        1644. Lowest Common Ancestor of a Binary Tree II
        If either node p or q does not exist in the tree, return null.
        All values of the nodes in the tree are unique.
        Time: O(N), Space: O(N)
        """
        parents = {root.val: None}
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node.left:
                parents[node.left.val] = node
                queue.append(node.left)
            if node.right:
                parents[node.right.val] = node
                queue.append(node.right)

        if p.val not in parents or q.val not in parents:
            return None

        ancestors = set()
        while p:
            ancestors.add(p.val)
            p = parents[p.val]
        while q and q.val not in ancestors:
            q = parents[q.val]
        return q


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        1644. Lowest Common Ancestor of a Binary Tree II
        If either node p or q does not exist in the tree, return null.
        All values of the nodes in the tree are unique.
        Time: O(N), Space: O(N)
        """
        def lca(node):
            """Return LCA of p and q in subtree rooted at node."""
            if not node:
                return None, 0
            left, x = lca(node.left)
            right, y = lca(node.right)

            if node in (p, q):
                return node, x+y+1
            if left and right:
                return node, x+y
            if left:
                return left, x
            else:
                return right, y

        res, count = lca(root)
        if count == 2:
            return res
        else:
            return None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        1650. Lowest Common Ancestor of a Binary Tree III
        Each node will have a reference to its parent node.
        """
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1 else q
            p2 = p2.parent if p2 else p
        return p1


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        1650. Lowest Common Ancestor of a Binary Tree III
        Each node will have a reference to its parent node.
        """
        seen = set()
        while q:
            seen.add(q.val)
            q = q.parent

        while p:
            if p.val in seen:
                return p
            seen.add(p.val)
            p = p.parent
        return None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        """
        1676. Lowest Common Ancestor of a Binary Tree IV
        All the nodes exist in the tree, and all node values are unique.
        Return LCA of all nodes. 
        """
        nodes = set(nodes)
        if not root or root in nodes:
            return root

        left = self.lowestCommonAncestor(root.left, nodes)
        right = self.lowestCommonAncestor(root.right, nodes)

        if left and right:
            return root
        else:
            return left or right


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        """    
        1123. Lowest Common Ancestor of Deepest Leaves
        At each node, compute the height of its left and right children.
        1) if left == right, return node
        2) if left > right, move to left node
        3) if left < right, move to right node
        Time: O(N), Space: O(N)
        """
        @lru_cache(None)
        def height(node):
            """Return height of tree rooted at node."""
            if not node:
                return 0
            left, right = height(node.left), height(node.right)
            return max(left, right) + 1

        node = root
        while node:
            left = height(node.left)
            right = height(node.right)
            if left == right:
                return node
            elif left > right:
                node = node.left
            else:
                node = node.right
        return node
