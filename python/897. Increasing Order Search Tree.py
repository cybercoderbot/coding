"""
897. Increasing Order Search Tree
Easy

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Example 1:
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:
Input: root = [5,1,7]
Output: [1,null,5,null,7]

"""

"""
Intuition
Don't need the condition of BST, just in-order output the whole tree.

Straight forward idea here:
result = inorder(root.left) + root + inorder(root.right)


Explanation
Recursively call function increasingBST(TreeNode root, TreeNode tail)
tail is its next node in inorder,
（the word next may be easier to understand, but it’s a keyword in python)

If root == null, the head will be tail, so we return tail directly.

we recursively call increasingBST(root.left, root),
change left subtree into the linked list + current node.

we recursively call increasingBST(root.right, tail),
change right subtree into the linked list + tail.

Now the result will be in a format of linked list, with right child is next node.
Since it's single linked list, so we set root.left = null.
Otherwise it will be TLE for Leetcode judgment to traverse over your tree.

The result now is increasingBST(root.left) + root + increasingBST(root.right).

One tip here, we should arrange the old tree, not create a new tree.
The leetcode judgment comparer only the values,
so it won't take it as wrong answer if you return a new tree,
but it is wrong.


Complexity
O(N) time traversal of all nodes
O(height) space
"""


class Solution:
    def increasingBST(self, root, tail=None):
        if not root:
            return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res


class Solution:
    def increasingBST(self, root):

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            node.left = None
            self.p.right = node
            self.p = node
            inorder(node.right)

        res = self.p = TreeNode(None)
        inorder(root)

        return res.right
