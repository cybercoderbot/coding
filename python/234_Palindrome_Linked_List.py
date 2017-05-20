# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 链表难的地方就在于不能通过坐标来直接访问，而只能从头开始遍历到某个位置。
        # 根据回文串的特点，我们需要比较对应位置的值是否相等，那么我们首先需要找到链表的中点，
        # 这个可以用快慢指针来实现，原理是fast和slow两个指针，每次快指针走两步，慢指针走一步，
        # 等快指针走完时，慢指针的位置就是中点。我们还需要用栈，每次慢指针走一步，都把值存入栈中，
        # 等到达中点时，链表的前半段都存入栈中了，由于栈的后进先出的性质，就可以和后半段链表按照
        # 回文对应的顺序比较了。代码如下：
        
        if not head or not head.next:
            return True
            
        slow = fast = head
        
        stack = []
        stack.append(head.val)
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)
            
        if not fast.next: stack.pop()
        
        while slow.next:
            slow = slow.next
            if slow.val != stack.pop():
                return False
        
        return True
            
            
            
            
            
            
        
