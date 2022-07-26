class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        # 排序（Sort）

        # 这道题给了我们一系列无序的时间点，让我们求最短的两个时间点之间的差值。
        # 那么最简单直接的办法就是给数组排序，这样时间点小的就在前面了，然后我们分别把小时和分钟提取出来，
        # 计算差值，注意唯一的特殊情况就是第一个和末尾的时间点进行比较，第一个时间点需要加上24小时再做差值

        # O(nlog(n)) sort Python
        # Very straight forward, convert time in timePoints into a sorted list then find the minimum difference
        # between the two neighbors. Remember to compare the biggest one with the smallest as the example shows.

        def helper(time):
            hour, minute = map(int, time.split(":"))
            return hour * 60 + minute

        times = sorted(helper(time) for time in timePoints)
        ans = 24 * 60
        for i in range(1, len(times)):
            ans = min(ans, times[i] - times[i-1])
        return min(24 * 60 + times[0] - times[-1], ans)
