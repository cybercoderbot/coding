"""
160. Intersection of Two Linked Lists
Easy
https://leetcode.com/problems/intersection-of-two-linked-lists/

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        p, q = headA, headB

        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA

        return p


"""
235. Lowest Common Ancestor of a Binary Search Tree
Easy

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.


Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Solution
Since this is a BST, we could utilize the symmetric order while traversing the tree. 
Starting from root, move left if we find that both p and q values are smaller than current node; 
move right if we find that both p and q values are greater than current node. Otherwise, 
return the node.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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


"""
236. Lowest Common Ancestor of a Binary Tree
Medium

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root or root in (p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right


"""
1644. Lowest Common Ancestor of a Binary Tree II
Medium

Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. 
If either node p or q does not exist in the tree, return null. All values of the nodes in the tree 
are unique.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 Breadth First Search
# The idea is simmilar with 1257, first visit all the nodes and record their parents, then use a set to store all the parents of one node and traverse the next node's ancestors to find the first parent in the set. \
# Complexity: O(n) in space, O(n) in time

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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

        def lca(node):
            """Return LCA of p and q in sub-tree rooted at node (if found)."""

            if node:
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

            return None, 0

        res, count = lca(root)

        if count == 2:
            return res
        else:
            return None


"""
1650. Lowest Common Ancestor of a Binary Tree III
Medium

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1 else q
            p2 = p2.parent if p2 else p

        return p1


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        while q:
            visited.add(q.val)
            q = q.parent

        while p:
            if p.val in visited:
                return p
            visited.add(p.val)
            p = p.parent

        return None


"""
1676. Lowest Common Ancestor of a Binary Tree IV
Medium

Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) 
of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        """Return LCA of all nodes."""

        nodes = set(nodes)

        if not root or root in nodes:
            return root

        left = self.lowestCommonAncestor(root.left, nodes)
        right = self.lowestCommonAncestor(root.right, nodes)

        if left and right:
            return root
        else:
            return left or right


"""
1123. Lowest Common Ancestor of Deepest Leaves
Medium

Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
"""

# Solution
# At each node, compute the height of its left and right children.

# if left == right, return node;
# if left > right, move to left node;
# if left < right, move to right node.


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        # Analysis
        # Time complexity O(N)
        # Space complexity O(N)

        def height(node):
            """Return height of tree rooted at node."""
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1

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
