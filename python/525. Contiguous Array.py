class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 这道题给了我们一个二进制的数组，让我们找邻近的子数组使其0和1的个数相等。
        # 对于求subarray的问题，我们需要时刻记着cumsum是一种很犀利的工具，但是这里怎么
        # 将子数组的和跟0和1的个数之间产生联系呢？我们需要用到一个trick，遇到1就加1，遇到0，就减1，
        # 这样如果某个子数组和为0，就说明0和1的个数相等。知道了这一点，我们用一个哈希表建立子数组之和跟
        # 结尾位置的坐标之间的映射。如果某个子数组之和在哈希表里存在了，说明当前子数组减去哈希表中存的
        # 那个子数字，得到的结果是中间一段子数组之和，必然为0，说明0和1的个数相等，我们更新结果ans

        ans = 0
        n = len(nums)
        nsum = 0

        d = {0: -1}

        for i in range(n):
            if nums[i] == 1:
                nsum += 1
            else:
                nsum -= 1
            if nsum not in d:
                d[nsum] = i
            else:
                ans = max(ans, i-d[nsum])

        return ans
