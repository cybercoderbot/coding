class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 解法: 栈（Stack）
        # 时间复杂度 O(n)

        # 对于循环数组的处理，将nums数组遍历两次，然后还是坐标i对len(nums)取余，取出数字，
        # 如果此时栈不为空，且栈顶元素小于当前数字，说明当前数字就是栈顶元素的右边第一个较大数，
        # 那么建立二者的映射，并且去除当前栈顶元素，最后如果i小于n，则把i压入栈。
        # 因为ans的长度必须是n，超过n的部分我们只是为了给之前栈中的数字找较大值，所以不能压入栈

        stack = []
        n = len(nums)
        ans = [-1] * n
        for x in range(2*n):
            i = x % n
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        return ans
