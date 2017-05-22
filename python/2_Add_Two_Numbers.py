# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 这道题，算法很简单，链表的数据类型也不难。就是建立一个新链表，
        # 然后把输入的两个链表从头往后，每两个相加，添加一个新节点到新链表后面，
        # 就是要处理下进位问题。还有就是最高位的进位问题要最后特殊处理一下.
        
        res = ListNode(None)
        current = res
        carry = 0
        
        while l1 or l2:
            if l1: num1 = l1.val
            else: num1 = 0
            
            if l2: num2 = l2.val
            else: num2 = 0
            
            addition = num1 + num2 + carry
            carry = addition / 10
            
            current.next = ListNode(addition%10)
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        if carry: 
            current.next = ListNode(1)
            
        return res.next
        
        
        
        
        
        
        
