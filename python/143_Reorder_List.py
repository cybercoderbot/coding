# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        
        # 解题思路：
        # 1. 利用快慢指针找到链表中点mid，将链表分为左右两半
        # 2. 将链表的右半部分in place reverse
        # 3. merge链表的左右两部分

        if not head or not head.next: return 
        
        # Find mid point
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        
        # cut the list in the middle    
        left = head
        right = mid.next
        if not right: return head
        mid.next = None
        
        # reverse the right half
        node = right.next
        right.next = None
        while node:
            next = node.next
            node.next = right
            right = node
            node = next
        
        # merge left and right
        dummy = ListNode(None)
        while left or right:
            if left:
                dummy.next = left
                left = left.next
                dummy = dummy.next
                
            if right:
                dummy.next = right
                right = right.next
                dummy = dummy.next
        
                
                
            
        
            
