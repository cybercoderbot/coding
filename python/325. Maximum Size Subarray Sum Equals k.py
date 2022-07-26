class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 给一个一维数组nums，让求和为k最大子数组，默认子数组必须连续，而且要在O(n)的时间复杂度完成。
        # 这就需要用哈希表和累积和来做，建立累积和的好处显而易见，若当前累积和正好等于k，那么从开头
        # 到此位置的子数组就是一个符合要求的解，但不一定是最长的子数组，我们可以用变量ans表示最长解，
        # 然后用每一个符合要求的解和最长解比较，来update ans

        d = {}
        cumsum = ans = 0

        for i in range(len(nums)):
            cumsum += nums[i]
            if cumsum not in d:
                d[cumsum] = i

            if cumsum == k:
                ans = i+1
            elif cumsum-k in d:
                ans = max(ans, i-d[cumsum-k])

        return ans
