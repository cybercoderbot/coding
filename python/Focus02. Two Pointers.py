class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        11. Container With Most Water
        """
        left, right = 0, len(height)-1
        res = 0
        while left < right:
            width = right - left
            depth = min(height[left], height[right])
            res = max(res,  width * depth)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        42. Trapping Rain Water (compute how much water it can trap in total)
        Keep track of the max height from forwards and backwards: left and right. 
        Use two pointers to scan the array until they meet with each other. 
        Any bars in the middle of left bar and right bar will not influence
        how much water the current positions can trap
        """
        i, j = 0, len(height)-1
        left, right, res = 0, 0, 0
        while i <= j:
            left = max(left, height[i])
            right = max(right, height[j])
            if left < right:
                res += left - height[i]
                i += 1
            else:
                res += right - height[j]
                j -= 1
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        42. Trapping Rain Water
        """
        i, j = 0, len(height)-1
        res = depth = 0
        while i < j:
            if height[i] <= height[j]:
                depth = max(depth, height[i])
                res += depth - height[i]
                i += 1
            else:
                depth = max(depth, height[j])
                res += depth - height[j]
                j -= 1
        return res


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        75. Sort Colors. 
        [2,0,2,1,1,0] -> [0,0,1,1,2,2]
        Dijkstra 3-way partitioning
        """
        left, mid, right = 0, 0, len(nums)-1
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
        return


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        84. Largest Rectangle in Histogram
        Use a stack to store non-decreasing height.
        At position i, pop all heights (by index) that's higher than current.
        Height is obtained from the poped index.
        Width is obtained by index i and last value on stack.
        """
        stack = []
        res = 0
        heights.append(0)
        for i, x in enumerate(heights):
            while stack and heights[stack[-1]] > x:
                depth = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                res = max(res, depth * width)
            stack.append(i)

        return res


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        167. Two Sum II - Input Array Is Sorted
        """
        left, right = 0, len(nums)-1
        while left < right:
            total = nums[left] + nums[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left+1, right+1]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        15. 3Sum, Sort nums -> 2sum using two pointers
        """
        if len(nums) < 3:
            return []

        nums.sort()

        N = len(nums)
        res = []
        for i in range(N):
            if i >= 1 and nums[i] == nums[i-1]:
                continue

            target = -1 * nums[i]
            left, right = i+1, N-1

            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        return res


class Solution:
    def isValid(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        """
        680. Valid Palindrome II
        True if the s is palindrome after deleting at most 1 character.
        """
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                x = self.isValid(s, i+1, j)
                y = self.isValid(s, i, j-1)
                return x or y
            i += 1
            j -= 1
        return True
