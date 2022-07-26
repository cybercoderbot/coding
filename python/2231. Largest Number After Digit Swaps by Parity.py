"""
905. Sort Array By Parity
Easy

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]
"""

"""
Since we are sorting even numbers ahead of odd numbers, below code will do.
If we sort odd numbers ahead of even numbers, set reverse flat to True.
"""


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        O(N) time & O(1) space solution
        """
        low, high = 0, len(nums)-1
        while low < high:
            if nums[low] % 2 == 0:
                low += 1
            elif nums[high] % 2 == 1:
                high -= 1
            else:
                nums[low], nums[high] = nums[high], nums[low]
        return nums


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        O(N) time & O(1) space solution
        """
        low = 0
        for high in range(len(nums)):
            if nums[high] % 2 == 0:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
        return nums


"""
2231. Largest Number After Digit Swaps by Parity
Easy

You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.

Example 1:
Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.

Example 2:
Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.
"""


class Solution:
    def largestInteger(self, num: int) -> int:

        odd, even = [], []
        for x in map(int, str(num)):
            if x & 1:
                odd.append(x)
            else:
                even.append(x)

        odd.sort()
        even.sort()

        res = 0
        for x in map(int, str(num)):
            if x & 1:
                res = 10*res + odd.pop()
            else:
                res = 10*res + even.pop()
        return res
