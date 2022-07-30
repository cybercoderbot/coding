"""
99. Recover Binary Search Tree
Medium

You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
"""


"""
Iteratively in-order traverse the tree. 
For a valid BST, the output should be in ascending order. 
Locate the two nodes where the symmetric order is violated, and swap their values.

"""


"""
Approach 2: Iterative Inorder Traversal
Intuition

Here we construct inorder traversal by iterations and identify swapped nodes at the same time, in one pass.

Iterative inorder traversal is simple: go left as far as you can, then one step right. Repeat till the end of nodes in the tree.

To identify swapped nodes, track the last node pred in the inorder traversal (i.e. the predecessor of the current node) and compare it with current node value. If the current node value is smaller than its predecessor pred value, the swapped node is here.

There are only two swapped nodes here, and hence one could break after having the second node identified.

Doing so, one could get directly nodes (and not only their values), and hence swap node values in O(1) time, drastically reducing the time needed for step 3.
"""


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        node = root
        x = y = pre = None

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if pre and node.val < pre.val:
                y = node
                if not x:
                    x = pre
                else:
                    break
            pre = node
            node = node.right

        x.val, y.val = y.val, x.val

        return


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node, stack = root, []
        pre = low = high = None

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
                continue
            node = stack.pop()

            # check symmetric order
            if pre and pre.val > node.val:
                if not low:
                    low, high = pre, node
                else:
                    high = node
            pre = node
            node = node.right

        low.val, high.val = high.val, low.val

        return
