"""
958. Check Completeness of a Binary Tree
Medium

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:
Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
"""


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        """
        The level-order traversal array of a complete binary tree will never 
        have a null node in between non-null nodes. 
        If we encounter a null node, all the following nodes should also be null, 
        otherwise it's not complete.
        """

        hasNull = False
        queue = [root]

        while queue:
            node = queue.pop(0)
            if not node:
                hasNull = True
                continue
            elif hasNull:
                return False
            queue.append(node.left)
            queue.append(node.right)

        return True


class Solution:

    def isCompleteTree(self, root):
        """
        Use BFS to do a level order traversal,
        add childrens to the BFS queue,
        until we met the first empty node.

        For a complete binary tree,
        there should not be any node after we met an empty one.

        Time O(N), Space O(N)
        """

        i, queue = 0, [root]
        while queue[i]:
            queue.append(queue[i].left)
            queue.append(queue[i].right)
            i += 1
        return not any(queue[i:])
