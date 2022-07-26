class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 这道题给了我们一个数组，让我们求和为k的连续子数组的个数
        # 看到这道题想着肯定要建立累加和数组啊，然后遍历累加和数组的每个数字，首先看其是否为k，
        # 是的话结果ans自增1，然后再加个往前的循环，这样可以快速求出所有的子数组之和，看是否为k

        # ans = 0
        # n = len(nums)

        # for i in range(n):
        #     cumsum = nums[i]
        #     if cumsum == k:
        #         ans += 1
        #     for j in range(i+1,n):
        #         cumsum += nums[j]
        #         if cumsum == k:
        #             ans += 1
        # return ans

        # 大家比较推崇的其实是这种解法，用一个哈希表来建立连续子数组之和跟其出现次数之间的映射，
        # 初始化要加入{0:1}这对映射，原因是我们的思路是遍历数组中的数字，用cumsum来记录到当前位置的累加和，
        # 我们建立哈希表的目的是为了让我们可以快速的查找cumsum-k是否存在，即是否有连续子数组的和为cumsum-k，
        # 如果存在的话，那么和为k的子数组一定也存在，这样当cumsum刚好为k的时候，那么数组从起始到当前位置的
        # 这段子数组的和就是k，满足题意，如果哈希表中实现没有count[0]项的话，这个符合题意的结果就无法累加到
        # 结果ans中， 这就是初始化的用途。

        ans = cumsum = 0
        count = collections.Counter()

        for n in nums:
            count[cumsum] += 1
            cumsum += n
            ans += count[cumsum-k]

        return ans
