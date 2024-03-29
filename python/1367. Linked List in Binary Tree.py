"""
1367. Linked List in Binary Tree
Medium

Given a binary tree root and a linked list with head as the first node. 
Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.
In this context downward path means a path that starts at some node and goes downwards.

Example 1:
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  

Example 2:
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true

Example 3:
Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
"""


class Solution:
    @lru_cache(None)
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """"
        Time O(N * min(L,H)), Space O(H)
        where N = tree size, H = tree height, L = list length.
        """
        @lru_cache(None)
        def sub(head, root):
            if not head:
                return True
            if not root:
                return False
            if root.val != head.val:
                return False
            left = sub(head.next, root.left)
            right = sub(head.next, root.right)
            return left or right

        if not head:
            return True
        if not root:
            return False

        left = self.isSubPath(head, root.left)
        right = self.isSubPath(head, root.right)
        return sub(head, root) or left or right
