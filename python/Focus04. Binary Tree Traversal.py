class Solution(object):
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Inorder: left -> root -> right
        """

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

        root = TreeNode(inorder[index])
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])

        return root


class Solution:
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

        root = TreeNode(val)
        # right -> left
        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)

        return root


class Solution:
    def buildTree(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        """
        889. Construct Binary Tree from Preorder and Postorder Traversal

        The first node in preorder and the last node in postorder are both value of the root. The Second last of postorder is value of right child of the root. 
        So we can find the index to split left and right children in preorder. 
        Don't forget to evaluate if the length of postorder > 1, since we used post[-2].
        """

        if not preorder or not postorder:
            return None

        root = TreeNode(preorder[0])
        if len(postorder) == 1:
            return root

        right = postorder[-2]
        index = preorder.index(right)

        root.left = self.buildTree(preorder[1: index], postorder[:index-1])
        root.right = self.buildTree(preorder[index:], postorder[index-1:-1])

        return root


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
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
        Trace-retrace via recursion
        """

        loc = {x: i for i, x in enumerate(inorder)}
        index = 1

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
