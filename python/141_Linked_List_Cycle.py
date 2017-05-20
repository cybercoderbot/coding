# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 这道题是快慢指针的经典应用。
        # 只需要设两个指针，一个每次走一步的慢指针和一个每次走两步的快指针，
        # 如果链表里有环的话，两个指针最终肯定会相遇。实在是太巧妙了，要是我肯定想不出来。代码如下：
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast: 
                return True
            
        return False
        
        
        
        
        
        
        
        
        
        
        
        
