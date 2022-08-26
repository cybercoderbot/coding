from collections import defaultdict


class Solution:
    @lru_cache(None)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Preorder: root -> left -> right
        """
        if not root:
            return []

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left + right


class Solution:
    @lru_cache(None)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Inorder: left -> root -> right
        """
        if not root:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] + right


class Solution:
    @lru_cache(None)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Postorder: left -> right -> root
        """
        if not root:
            return []

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        return left + right + [root.val]


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Preorder: root -> left -> right
        """
        @lru_cache(None)
        def preorder(node):
            if not node:
                return []

            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        res = []
        preorder(root)
        return res


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """
        589. N-ary Tree Preorder Traversal
        root -> children
        """
        if not root:
            return []
        res = [root.val]
        for child in root.children:
            res.extend(self.preorder(child))
        return res


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        590. N-ary Tree Postorder Traversal
        """
        if not root:
            return []
        res = []
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """
        589. N-ary Tree Preorder Traversal
        root -> children
        """
        @lru_cache(None)
        def traverse(node):
            if not node:
                return
            res.append(node.val)
            for child in node.children:
                traverse(child)

        res = []
        traverse(root)
        return res


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        590. N-ary Tree Postorder Traversal
        children -> root
        """
        def traverse(node):
            if not node:
                return
            for child in node.children:
                traverse(child)
            res.append(node.val)

        res = []
        traverse(root)
        return res


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """
        589. N-ary Tree Preorder Traversal
        root -> children
        """
        if not root:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.extend(node.children[::-1])
        return res


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        590. N-ary Tree Postorder Traversal
        children -> root
        """
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.extend(node.children)
        return res[::-1]


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        429. N-ary Tree Level Order Traversal
        """
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            vals, level = [], []
            for node in queue:
                vals.append(node.val)
                for child in node.children:
                    if child:
                        level.append(child)
            res.append(vals)
            queue = level
        return res


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Inorder: left -> root -> right
        """
        @lru_cache(None)
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        res = []
        inorder(root)
        return res


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Postorder: left -> right -> root
        """
        @lru_cache(None)
        def postorder(node):
            if not node:
                return []
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

        res = []
        postorder(root)
        return res


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        102. Binary Tree Top-Down Level Order Traversal
        """
        if not root:
            return

        res, queue = [], [root]
        while queue:
            level, vals = [], []
            for node in queue:
                vals.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            res.append(vals)
            queue = level

        return res


class Solution:
    def levelOrder(self, root: Optional['Node']) -> List[List[int]]:
        """
        429. N-ary Tree Level Order Traversal
        """
        if root is None:
            return []

        res = []
        queue = [root]
        while queue:
            vals, level = [], []
            for node in queue:
                vals.append(node.val)
                level.extend(node.children)
            res.append(vals)
            queue = level
        return res


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        107. Binary Tree Bottom-Up Level Order Traversal II
        """
        if not root:
            return []

        res, queue = [], [root]
        while queue:
            vals, level = [], []
            for node in queue:
                vals.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            res.append(vals)
            queue = level

        return res[::-1]


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        103. Binary Tree Zigzag Level Order Traversal
        """
        if not root:
            return []

        res, queue = [], [root]
        forward = True
        while queue:
            vals, level = [], []
            for node in queue:
                vals.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            res.append(vals if forward else vals[::-1])
            queue = level
            forward = not forward

        return res


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        314. Binary Tree Vertical Order Traversal
        queue: (col, node). seen: {col: [node.val]}
        left: (col-1, node.left), right: (col+1, node.right)
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        tree = collections.defaultdict(list)
        queue = collections.deque([(0, root)])
        while queue:
            col, node = queue.popleft()
            tree[col].append(node.val)
            if node.left:
                queue.append((col-1, node.left))
            if node.right:
                queue.append((col+1, node.right))

        return [tree[x] for x in sorted(tree.keys())]


class Solution:
    @lru_cache(None)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        105. Construct Binary Tree from Preorder and Inorder Traversal
        Inorder:  left -> root -> right
        Preorder: root -> left -> right
        The 1st node in preorder is the root of the tree. Let it be x

        Elements left to x in inorder form the LEFT subtree.
        Elements right to x in inorder forms the RIGHT subtree.

        Build left subtree, then build right subtree.
        """
        if not inorder or not preorder:
            return None

        val = preorder.pop(0)
        index = inorder.index(val)

        root = TreeNode(val=val)
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])

        return root


class Solution:
    @lru_cache(None)
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        106. Construct Binary Tree from Inorder and Postorder Traversal
        Inorder:   left -> root -> right
        Postorder: left -> right -> root
        The last node in postorder is the root of the tree. 
        Build right subtree, then build left subtree.
        """
        if not inorder or not postorder:
            return None

        val = postorder.pop()
        index = inorder.index(val)

        root = TreeNode(val=val)
        # right -> left
        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)

        return root


class Solution:
    def buildTree(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        """
        889. Construct Binary Tree from Preorder and Postorder Traversal

        The first node in preorder and the last node in postorder are both value of the root. 
        The Second last of postorder is value of RIGHT child of the root. 
        So we can find the index to split left and right children in preorder. 
        Don't forget to evaluate if the length of postorder > 1, since we used post[-2].
        """
        if not preorder or not postorder:
            return None

        root = TreeNode(val=preorder[0])
        if len(preorder) == 1:
            return root

        right = postorder[-2]
        index = preorder.index(right)

        root.left = self.buildTree(preorder[1: index], postorder[:index-1])
        root.right = self.buildTree(preorder[index:], postorder[index-1:-1])

        return root


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        106. Construct Binary Tree from Inorder and Postorder Traversal
        Trace-retrace via stack
        """
        # mapping from val to pos
        loc = {x: i for i, x in enumerate(inorder)}
        root = None
        stack = []

        for x in reversed(postorder):
            if not root:
                root = node = TreeNode(x)
            elif loc[node.val] < loc[x]:
                stack.append(node)
                node.right = node = TreeNode(x)
            else:
                while stack and loc[x] < loc[stack[-1].val]:
                    node = stack.pop()
                node.left = node = TreeNode(x)
        return root


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        106. Construct Binary Tree from Inorder and Postorder Traversal
        Trace-retrace via recursion
        """
        loc = {x: i for i, x in enumerate(inorder)}
        index = 1

        @lru_cache(None)
        def build(left, right):
            nonlocal index

            if left > right:
                return None

            node = TreeNode(postorder[-index])
            index += 1
            mid = loc[node.val]
            node.right = build(mid+1, right)
            node.left = build(left, mid-1)

            return node

        return build(0, len(inorder)-1)


class Solution:
    def buildTree(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        """
        889. Construct Binary Tree from Preorder and Postorder Traversal
        """
        stack = [TreeNode(preorder[0])]
        i = 0
        for x in preorder[1:]:
            node = TreeNode(x)
            while stack[-1].val == postorder[i]:
                stack.pop()
                i += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)

        return stack[0]


class Solution:
    def recoverFromPreorder(self, s: str) -> TreeNode:
        """
        1028. Recover a Tree From Preorder Traversal
        """
        if not s:
            return None

        stack = []
        depth, val = 0, ""
        for i, c in enumerate(s):
            if c.isdigit():
                val += s[i]
                if i+1 == len(s) or s[i+1] == "-":
                    node = TreeNode(int(val))
                    while len(stack) > depth:
                        stack.pop()
                    if stack:
                        if not stack[-1].left:
                            stack[-1].left = node
                        else:
                            stack[-1].right = node
                    stack.append(node)
                    depth = 0
            elif c == "-":
                depth += 1
                val = ""

        return stack[0]
