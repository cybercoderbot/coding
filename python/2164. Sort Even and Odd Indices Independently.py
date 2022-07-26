"""
2164. Sort Even and Odd Indices Independently
Easy

You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:

Sort the values at odd indices of nums in non-increasing order.
For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd indices 1 and 3 are sorted in non-increasing order.
Sort the values at even indices of nums in non-decreasing order.
For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at even indices 0 and 2 are sorted in non-decreasing order.
Return the array formed after rearranging the values of nums.

 

Example 1:

Input: nums = [4,1,2,3]
Output: [2,3,4,1]
Explanation: 
First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,1,2,3] to [4,3,2,1].
Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
So, nums changes from [4,1,2,3] to [2,3,4,1].
Thus, the array formed after rearranging the values is [2,3,4,1].
Example 2:

Input: nums = [2,1]
Output: [2,1]
Explanation: 
Since there is exactly one odd index and one even index, no rearrangement of values takes place.
The resultant array formed is [2,1], which is the same as the initial array. 
"""


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = sorted(nums[::2])
        odd = sorted(nums[1::2], reverse=True)
        nums[::2], nums[1::2] = even, odd
        return nums


class Solution:

    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums

        odd, even = [], []
        for k in range(len(nums)):
            if k % 2 == 0:
                even.append(nums[k])
            else:
                odd.append(nums[k])

        even.sort()
        odd.sort(reverse=True)

        i = j = 0
        for k in range(len(nums)):
            if k % 2 == 0:
                nums[k] = even[i]
                i += 1
            else:
                nums[k] = odd[j]
                j += 1

        return nums


"""
922. Sort Array By Parity II
Easy

Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

 

Example 1:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2:
Input: nums = [2,3]
Output: [2,3]

Even & odd indices

maintain two indices "even" and "odd" which start at 0 and 1 spectively
loop through elements in array
if element is odd, copy it to position of "odd" index and increase odd by two
if element is even, copy it to positon of "even" index and increase even by two.

"""


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd, N = 0, 1, len(nums)

        while even < N and odd < N:
            if nums[even] % 2 == 0:
                even += 2
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                odd += 2
        return nums


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = [], []

        for n in nums:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even.pop()
            else:
                nums[i] = odd.pop()

        return nums


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = 1
        for even in range(0, len(nums), 2):
            if nums[even] % 2 != 0:
                while nums[odd] % 2 == 1:  # This line is critical to use `while` not `if`
                    odd += 2
                nums[even], nums[odd] = nums[odd], nums[even]
        return nums


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        index = [0, 1]  # even & odd indices
        for x in nums:
            res[index[x % 2]] = x
            index[x % 2] += 2
        return res


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
        An alternative implementation that updates nums in place.
        """
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if not nums[i] & 1:
                i += 2
            elif nums[j] & 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
        return nums
