"""
136. Single Number
Easy

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""


from collections import Counter
from operator import xor
from functools import reduce


"""
Algorithm
Utilizing the fact that 
x ^ x = 0 and 
x ^ 0 = x, 
one could sequentially xor the elements to find the unique one.

Time complexity O(N)
Space complexity O(1)

"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res ^= x
        return res


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)


"""
137. Single Number II
Medium

Given an integer array nums where every element appears three times except for one, 
which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
 

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
"""


"""
O(N) space 
Define frequency table to count the occurrence of numbers and return the one which only appears once. 
This is not the most efficient approach but is extremely practical.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        return next(k for k, v in freq.items() if v == 1)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[-1][0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums))*3 - sum(nums))//2


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = Counter(nums)
        return sorted(d, key=d.get)[0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for n in nums:
        #     if nums.count(n) == 1:
        #         return n
        return next(n for n in nums if nums.count(n) == 1)


"""
260. Single Number III
Medium

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]"""


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = defaultdict(lambda: 0)

        for n in nums:
            freq[n] += 1

        res = []
        for key in freq:
            if freq[key] == 1:
                res.append(key)

        return res


"""
268. Missing Number
Easy

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 
Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Approach 1 - bit manipulation

        If we augment nums with 1, ..., n and xor all of them, what's returned is the missing number. 
        This utilizes the fact that x ^ x = 0 and x ^ 0 = x.

        """
        return reduce(xor, (i ^ x for i, x in enumerate(nums, 1)))


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Approach 2 - math (Gauss's formula)
        """
        N = len(nums)
        return N*(N+1)//2 - sum(nums)


"""
287. Find the Duplicate Number
Medium

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Sort, O(NlogN) time & O(1) space
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Use a hash set to remember what element has been seen 
        O(N) time and O(N) space.
        """
        seen = set()
        for x in nums:
            if x in seen:
                return x
            seen.add(x)

        return


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Mark the element if its index corresponding to the number has 
        been seen. When we encounter the marked index again, return it 
        O(N) time, O(1) space
        """
        for x in nums:
            i = abs(x) - 1
            if nums[i] < 0:
                return i+1
            nums[i] *= -1

        return


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        The solution is intellectually stimulating, but not practical. The idea is to consider the array as a linked list. The elements are the indices and the values refer to the nodes they point to. Following such structure, the duplicated number means that there are at least two nodes pointing to it. As a result, there is a cycle in the linked list.
        """
        fast = slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow
