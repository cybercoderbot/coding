"""
80. Remove Duplicates from Sorted Array II
Medium


Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        for n in nums:
            count = nums.count(n)
            if count > 2:
                for j in range(count-2):
                    nums.remove(n)
        return len(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        # Time complexity O(N)
        # Space complexity O(1)
        """
        i = 0
        for n in nums:
            if i < 2 or nums[i-2] < n:
                nums[i] = n
                i += 1
        return i


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 2:
            return N

        i, j, count = 0, 1, 1

        while j < N:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                count = 1
            elif nums[i] == nums[j] and count < 2:
                count += 1
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1
