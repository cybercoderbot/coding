class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 这道题让我们求最大连续1的个数，我们可以遍历一遍数组，用一个计数器cnt来统计1的个数，
        # 方法是如果当前数字为0，那么cnt重置为0，如果不是0，cnt自增1，然后每次更新结果ans即可

        cnt, ans = 0, 0

        for n in nums:
            if n == 1:
                cnt += 1
            else:
                cnt = 0

            ans = max(ans, cnt)
        return ans
