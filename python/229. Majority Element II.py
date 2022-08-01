"""
229. Majority Element II
Medium

Given an integer array of size n, find all elements that appear more than n/3 times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]"""


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        """
        1150. Check If a Number Is Majority Element in a Sorted Array
        Brute force: O(N)
        """
        count = 0
        for x in nums:
            if x == target:
                count += 1
            else:
                count -= 1
        return count > 0


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        """
        1150. Check If a Number Is Majority Element in a Sorted Array
        Binary search: O(logN)
        """
        if target != nums[(len(nums)-1)//2]:
            return False

        def bisect_left(arr, tgt, low, high):
            while low < high:
                mid = (low + high)//2
                if arr[mid] >= tgt:
                    high = mid
                else:
                    low = mid+1
            return low

        low = bisect_left(nums, target, 0, len(nums)//2)
        return nums[low + len(nums)//2] == target


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """169. Majority Element. Boyer-Moore majority voting alg"""
        res = vote = 0
        for x in nums:
            if vote == 0:
                res = x
            if x == res:
                vote += 1
            else:
                vote -= 1
        return res


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        169. Majority Element. Boyer-Moore algorithm.
        """
        freq = defaultdict(int)
        res = freq[res] = -1
        for x in nums:
            freq[x] += 1
            if freq[res] < freq[x]:
                res = x
        return res


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Boyer-Moore algorithm. Here, we use two place holders res and two counters vote to record the element satisfying the requirement. Given a new element x, if it matches a place-holding element, increment its count by 1. If it matches neither, decrement both their counts by 1.
        """
        res, vote = [None]*2, [0]*2
        for x in nums:
            if vote[0] == 0 and x not in res:
                res[0] = x
            elif vote[1] == 0 and x not in res:
                res[1] = x

            if res[0] == x:
                vote[0] += 1
            elif res[1] == x:
                vote[1] += 1
            else:
                vote = [x-1 for x in vote]
        return [x for x in res if nums.count(x) > len(nums)//3]


class Solution:
    def majorityElement(self, nums: List[int], N=2) -> List[int]:
        """
        This can be extended to a given integer N.
        """
        res, vote = [None]*N, [0]*N
        for x in nums:
            for i in range(N):
                if vote[i] == 0 and x not in res:
                    res[i] = x
                    break
            for i in range(N):
                if res[i] == x:
                    vote[i] += 1
                    break
            else:
                vote = [x-1 for x in vote]
        return [x for x in res if nums.count(x) > len(nums)//(N+1)]
