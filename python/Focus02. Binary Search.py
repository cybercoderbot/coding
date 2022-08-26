"""
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/769703/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
"""

"""
Most Generalized Binary Search
Suppose we have a search space.
It could be an array, a range, etc.
Usually it's sorted in ascend order.

For most tasks, we can transform it into the following generalized form:
Minimize k, s.t. condition(k) is True

1. Correctly initialize the boundary variables left and right.
Only one rule: set up the boundary to include all possible elements
2. Decide return value. Is it return left or return left - 1?
Rule of thumb: after exiting the while loop, left is the minimal k satisfying the condition
3. Design the condition function. This is the most difficult part. Needs lots of practice.
"""


class Solution:
    def binarySearch(array) -> int:
        def condition(value) -> bool:
            pass

        left, right = 0, len(array)
        while left < right:
            mid = (left + right) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        35. Search Insert Position
        """
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left


class Solution:
    def mySqrt(self, target: int) -> int:
        """
        69. Sqrt(x)
        """
        if target <= 1:
            return target

        left, right = 1, target
        while left < right:
            mid = (left + right) // 2
            if mid * mid > target:
                right = mid
            else:
                left = mid + 1
        return left-1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        33. Search in Rotated Sorted Array
        nums = [4,5,6,7,0,1,2], target = 0, output: 4
        nums = [4,5,6,7,0,1,2], target = 3, output: -1
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


class Solution:
    def firstBadVersion(self, n) -> int:
        """
        278. First Bad Version [Easy]
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        """
        774. Minimize Max Distance to Gas Station
        """
        eps = 1e-6
        left, right = eps, nums[-1] - nums[0]
        while left + eps < right:
            mid = (left + right) / 2
            count = 0
            for x, y in zip(nums[:-1], nums[1:]):
                count += math.ceil((y - x) / mid) - 1
            if count <= k:
                right = mid
            else:
                left = mid
        return right


class Solution:
    def splitArray(nums: List[int], m: int) -> int:
        """
        410. Split Array Largest Sum
        """
        def feasible(thres) -> bool:
            total, splits = 0, 1
            for x in nums:
                total += x
                if total > thres:
                    total = x
                    splits += 1
            return splits <= m

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        """
        875. Koko Eating Bananas
        Given speed x, we could compute the time for Koko to eat all banana.
        We could binary search in the speed space for the slowest speed for Koko to
        eat all banana within H hours.
        """
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if sum(ceil(x/mid) for x in piles) <= H:
                right = mid
            else:
                left = mid + 1
        return left


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """
        668. Kth Smallest Number in Multiplication Table
        """
        def enough(num) -> bool:
            count = 0
            # count row by row
            for val in range(1, m + 1):
                add = min(num // val, n)
                # early exit
                if add == 0:
                    break
                count += add
            return count >= k

        left, right = 1, n * m
        while left < right:
            mid = (left + right) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        1011. Capacity To Ship Packages Within Days
        """
        def canShip(capacity):
            """True if possible to deliver all packages of given capacity."""
            res, val = 0, inf
            for w in weights:
                if val + w > capacity:
                    res += 1
                    val = 0
                val += w
            return res <= D

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        return left


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        """
        1011. Capacity To Ship Packages Within Days
        """
        def feasible(capacity) -> bool:
            days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:
                    total = weight
                    days += 1
            return days <= D

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        """
        1231. Divide Chocolate
        """
        left, right = 0, sum(sweetness) // (k + 1)
        while left < right:
            mid = (left + right + 1) // 2
            pieces = total = 0
            for x in sweetness:
                total += x
                if total >= mid:
                    total = 0
                    pieces += 1
            if pieces < k+1:
                right = mid - 1
            else:
                left = mid
        return left


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        1482. Minimum Number of Days to Make m Bouquets
        """
        if m * k > len(bloomDay):
            return -1

        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            flower, bouquet = 0, 0
            for x in bloomDay:
                if x > mid:
                    flower = 0
                else:
                    flower += 1
                if flower >= k:
                    flower = 0
                    bouquet += 1
                    if bouquet == m:
                        break
            if bouquet == m:
                right = mid
            else:
                left = mid + 1
        return left


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        1482. Minimum Number of Days to Make m Bouquets
        """
        def feasible(days) -> bool:
            bonquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bonquets >= m

        if len(bloomDay) < m * k:
            return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left


class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        """
        1539. Kth Missing Positive Number
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # ideally, nums[i] should hold i + 1 value
            # eg. nums[0] = 1, nums[1] = 2, ...
            missing = nums[mid] - (mid + 1)
            if missing >= k:
                right = mid - 1
            else:
                left = mid + 1
        return right + k + 1


class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        """
        1539. Kth Missing Positive Number
        Assume the final result is N,
        And there are m number not missing in the range of [1, N].
        Binary search the m in range [0, len(nums)].

        If there are m number not missing,
        that is nums[0], nums[1] .. nums[m-1],
        the number of missing under nums[m] is nums[m] - 1 - m.

        If nums[m] - 1 - m < k, m is too small, we update left = m.
        If nums[m] - 1 - m >= k, m is big enough, we update right = m.

        Note that, we exit the while loop, left = r,
        which equals to the number of missing number used.
        So the Kth positive number will be left + k.
        Time O(logN), Space O(1)
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] - mid <= k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k
