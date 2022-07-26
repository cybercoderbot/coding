class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # 解题思路：
        # 动态规划（Dynamic Programming）
        # 利用数组dp[i]记录和为i的子数组是否存在，初始令dp[0] = 1

        # for n in nums:
        #     for i in range(sum(nums) - n + 1):
        #         if dp[i]: dp[i + n] = 1

        if sum(nums) & 1:
            return False

        target = sum(nums) / 2

        nset = set([0])
        for n in nums:
            # if you need the original set unchanged when the new set is modified,
            # you can use copy() method. This is called shallow copy.
            for m in nset.copy():
                nset.add(m + n)
        return target in nset
