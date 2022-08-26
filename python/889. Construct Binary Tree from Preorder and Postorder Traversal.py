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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Trace-retrace via stack
        """
        d = {x: i for i, x in enumerate(inorder)}

        def build(low, high):
            if low > high:
                return None

            node = TreeNode(postorder.pop())
            mid = d[node.val]
            node.right = build(mid+1, high)
            node.left = build(low, mid-1)

            return node

        return build(low=0, high=len(inorder)-1)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Trace-retrace via recursion
        """
        @lru_cache(None)
        def build(left, right):
            nonlocal index

            if left > right:
                return None

            node = TreeNode(postorder[-index])
            index += 1
            mid = d[node.val]
            node.right = build(mid+1, right)
            node.left = build(left, mid-1)

            return node

        d = {x: i for i, x in enumerate(inorder)}
        index = 1

        return build(0, len(inorder)-1)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Time: O(N), Space: O(N)
        """
        d = {x: i for i, x in enumerate(inorder)}  # relative position
        root = None
        stack = []
        for x in reversed(postorder):
            if not root:
                root = node = TreeNode(x)
            elif d[x] > d[stack[-1].val]:
                stack[-1].right = node = TreeNode(x)
            else:
                while stack and d[stack[-1].val] > d[x]:
                    node = stack.pop()  # retrace
                node.left = node = TreeNode(x)
            stack.append(node)
        return root


"""
889. Construct Binary Tree from Preorder and Postorder Traversal
Medium

Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

Example 1:
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Example 2:
Input: preorder = [1], postorder = [1]
Output: [1]
"""

"""

Background
Given a binary tree, there are 3 orders to traverse it: preorder, inorder and postorder,
all of which are widely used in practice. Conversely, if a traversal result is provided, one cannot
recreate the binary tree as differently structued binary trees could result in the same traversal.
But if two traversals are given, then it is possible to build the tree, which is what 105, 106 and 889 are about.

105. Construct Binary Tree from Preorder and Inorder Traversal
106. Construct Binary Tree from Inorder and Postorder Traversal
889. Construct Binary Tree from Preorder and Postorder Traversal

Iterative approach
Here, we scan through one vector while using the other one to decide to go deeper on the tree or retrace
to higher level. In this iterative approach we use a stack to store the nodes that we've visited and can
potentially go back to.

"""


"""
Foreword
I saw some solutions saying O(N) time, but actually they are not.
If it takes already O(N) time to find left part and right part, it could not be O(N).

Complexity:
Time O(N), as we iterate both pre index and post index only once.
Space O(height), depending on the height of constructed tree.


Recursive Solution
Create a node TreeNode(pre[preIndex]) as the root.

Becasue root node will be lastly iterated in post order,
if root.val == post[posIndex],
it means we have constructed the whole tree,

If we haven't completed constructed the whole tree,
So we recursively constructFromPrePost for left sub tree and right sub tree.

And finally, we'll reach the posIndex that root.val == post[posIndex].
We increment posIndex and return our root node.
"""


class Solution:
    def buildTree(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        """
        The first element in preorder and the last element in postorder are both be the value of the root. The second to last of postorder should be the value of right child of the root. So we can find the index to split left and right children in preorder. Don't forget to evaluate if the length of postorder is larger than 1, since we used post[-2].
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

    preIndex, posIndex = 0, 0

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Create a node TreeNode(preorder[preIndex]) as the root.

        Becasue root node will be lastly iterated in post order,
        if root.val == post[posIndex],
        it means we have constructed the whole tree,

        If we haven't completed constructed the whole tree,
        So we recursively constructFromPrePost for left sub tree and right sub tree.

        And finally, we'll reach the posIndex that root.val == post[posIndex].
        We increment posIndex and return our root node.
        """

        root = TreeNode(preorder[self.preIndex])
        self.preIndex += 1

        if root.val != postorder[self.posIndex]:
            root.left = self.constructFromPrePost(preorder, postorder)

        if root.val != postorder[self.posIndex]:
            root.right = self.constructFromPrePost(preorder, postorder)

        self.posIndex += 1

        return root


"""
Iterative Solution
We will preorder generate TreeNodes, push them to stack and postorder pop them out.

Iterate on pre array and construct node one by one.
stack save the current path of tree.
node = new TreeNode(pre[i]), if not left child, add node to the left. otherwise add it to the right.
If we meet a same value in the pre and post, it means we complete the construction for current subtree. We pop it from stack.
"""


class Solution:
    def constructFromPrePost(self, pre, post):
        stack = [TreeNode(pre[0])]
        j = 0
        for val in pre[1:]:
            node = TreeNode(val)
            while stack[-1].val == post[j]:
                stack.pop()
                j += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
