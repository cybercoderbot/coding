# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        # 这道求两个链表的交点题要求执行时间为O(n)，则不能利用类似冒泡法原理去暴力查找相同点，
        # 事实证明如果链表很长的话，那样的方法效率很低。我也想到会不会是像之前删除重复元素的题
        # 一样需要用两个指针来遍历，可是想了好久也没想出来怎么弄。
        # 其实解法很简单，因为如果两个链长度相同的话，那么对应的一个个比下去就能找到，所以只需
        # 要把长链表变短即可。具体算法为：分别遍历两个链表，得到分别对应的长度。然后求长度的差值，
        # 把较长的那个链表向后移动这个差值的个数，然后一一比较即可。代码如下：

        if not headA or not headB:
            return None
        lenA = self.get_length(headA)
        lenB = self.get_length(headB)

        if lenA < lenB:
            for i in range(lenB-lenA):
                headB = headB.next
        else:
            for i in range(lenA-lenB):
                headA = headA.next

        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next

        if headA and headB:
            return headA
        else:
            return headB

    def get_length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
