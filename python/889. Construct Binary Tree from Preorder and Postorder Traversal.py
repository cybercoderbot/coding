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
But if two traversals are given, then it is possible to build the tree, which is what 105, 106 and 889 
on LC are about.

105. Construct Binary Tree from Preorder and Inorder Traversal
106. Construct Binary Tree from Inorder and Postorder Traversal
889. Construct Binary Tree from Preorder and Postorder Traversal

Iterative approach
Here, we scan through one vector while using the other one to decide to go deeper on the tree or retrace 
to higher level. In this iterative approach we use a stack to store the nodes that we've visited and can 
potentially go back to.

"""

# 105

"""

105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]


Solution

Inorder Traversal -> LEFT -> ROOT ->RIGHT
PreOrder Traversal -> ROOT -> LEFT -> RIGHT

We have two observations :

The first element in preorder is the root of the tree. Let it be x
Elements left to x in inorder form the LEFT subtree.
Elements right to x in inorder forms the RIGHT subtree.
image

Recursive Approach

BASE CASE -> If the array inorder is empty. -> RETURN
SELF WORK -> Create a new node with the value preorder[0] as first element is the root of the tree.
Recursion ->

Let the index of preorder[0] in inorder be INDEX.
Recursivly create left subtree by passing -> preorder with first element removed and the part of inorder array that lies to the left of INDEX. ->inorder[:INDEX]
Recursivly create right subtree by passing -> the part of inorder array that lies to the right of INDEX. ->inorder[:INDEX]
"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not inorder:
            return None

        RVAL = preorder.pop(0)
        INDEX = inorder.index(RVAL)

        root = TreeNode(inorder[INDEX])
        root.left = self.buildTree(preorder, inorder[:INDEX])
        root.right = self.buildTree(preorder, inorder[INDEX+1:])

        return root


# 106


class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        ROOTVAL = postorder.pop()
        root = TreeNode(ROOTVAL)
        INDEX = inorder.index(ROOTVAL)  # Line A

        root.right = self.buildTree(inorder[INDEX+1:], postorder)  # Line B
        root.left = self.buildTree(inorder[:INDEX], postorder)    # Line C

        return root


class Solution:
    def buildTree(self, inorder, postorder):

        mp = {val: i for i, val in enumerate(inorder)}

        def dfs(low, high):
            if low > high:
                return None

            node = TreeNode(postorder.pop())
            mid = mp[node.val]
            node.right = dfs(mid+1, high)
            node.left = dfs(low, mid-1)

            return node

        return dfs(0, len(inorder)-1)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def build(left, right):
            nonlocal index

            if left > right:
                return None

            node = TreeNode(postorder[-index])
            index += 1
            mid = mp[node.val]
            node.right = build(mid+1, right)
            node.left = build(left, mid-1)

            return node

        mp = {v: i for i, v in enumerate(inorder)}
        index = 1
        return build(0, len(inorder)-1)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Time complexity O(N)
        Space complexity O(N)
        """

        mp = {x: i for i, x in enumerate(inorder)}  # relative position
        root = None
        stack = []
        for x in reversed(postorder):
            if not root:
                root = node = TreeNode(x)
            elif mp[x] > mp[stack[-1].val]:
                stack[-1].right = node = TreeNode(x)
            else:
                while stack and mp[stack[-1].val] > mp[x]:
                    node = stack.pop()  # retrace
                node.left = node = TreeNode(x)
            stack.append(node)
        return root


# 889


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

    preIndex, posIndex = 0, 0

    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:

        root = TreeNode(pre[self.preIndex])
        self.preIndex += 1

        if root.val != post[self.posIndex]:
            root.left = self.constructFromPrePost(pre, post)

        if root.val != post[self.posIndex]:
            root.right = self.constructFromPrePost(pre, post)

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
