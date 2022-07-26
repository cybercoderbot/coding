class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

        # 用哈希表建立每个数字和其右边第一个较大数之间的映射，没有的话就是-1。
        # 我们遍历原数组中的所有数字，如果此时栈不为空，且栈顶元素小于当前数字，
        # 说明当前数字就是栈顶元素的右边第一个较大数，那么建立二者的映射，并且
        # 去除当前栈顶元素，最后将当前遍历到的数字压入栈。当所有数字都建立了映射，
        # 那么最后我们可以直接通过哈希表快速的找到子集合中数字的右边较大值

        d = {}
        s = []
        ans = []

        for n in nums:
            while s and s[-1] < n:
                d[s.pop()] = n
            s.append(n)

        for n in findNums:
            ans.append(d.get(n, -1))

        return ans
