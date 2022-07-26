class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # 这道求装最多水的容器的题和那道 Trapping Rain Water 收集雨水 很类似，但又有些不同，
        # 那道题让求整个能收集雨水的量，这道只是让求最大的一个的装水量，而且还有一点不同的是，
        # 那道题容器边缘不能算在里面，而这道题却可以算，相比较来说还是这道题容易一些，我们需要
        # 定义i和j两个指针分别指向数组的左右两端，然后两个指针向中间搜索，每移动一次算一个值和
        # 结果比较取较大的，容器装水量的算法是找出左右两个边缘中较小的那个乘以两边缘的距离

        n = len(height)
        ans = 0
        left, right = 0, n-1

        while left < right:
            depth = min(height[left], height[right])
            ans = max(ans,  (right - left) * depth)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
