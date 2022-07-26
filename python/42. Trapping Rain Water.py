class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # 这道收集雨水的题跟之前的那道 Largest Rectangle in Histogram 直方图中最大的矩形有些类似，
        # 但是又不太一样，我们先来看一种方法，这种方法是基于动态规划Dynamic Programming的，我们维护一个一维的dp数组，
        # 这个DP算法需要遍历两遍数组，第一遍遍历dp[i]中存入i位置左边的最大值，然后开始第二遍遍历数组，第二次遍历时
        # 找右边最大值，然后和左边最大值比较取其中的较小值，然后跟当前值A[i]相比，如果大于当前值，则将差值存入结果

        n = len(height)
        ans = 0
        lmax = rmax = 0

        dp = [0] * n

        for i in range(n):
            dp[i] = lmax
            lmax = max(lmax, height[i])

        for i in range(n-1, -1, -1):
            dp[i] = min(dp[i], rmax)
            rmax = max(rmax, height[i])
            if dp[i] > height[i]:
                ans += dp[i] - height[i]

        return ans
