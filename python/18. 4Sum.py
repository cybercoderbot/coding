"""
18. 4Sum
Medium

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

start by sorting the nums array, and iterates through the length of nums array,

i is the first district number, iterates through 0 to (n-1)
j is the second distict number, iterates through j+1 to (n-1)
k is the third distict number, iterates through k+1 until before idx for m
m is the last distict number.
In each iteration, we calculate the sums of i+j+k+m

if sum is equal to target and not yet included into answer, then [i,j,k,m] stored to res.
if the sum < target, increment c
if sum > target, decrement d
repeat the whole process until all conditions exhausted.

"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        4Sum: sort
        """
        res, N = [], len(nums)
        nums.sort()

        for i in range(N):
            for j in range(i+1, N):
                left, right = j+1, N-1

                while left < right:
                    sums = nums[i] + nums[j] + nums[left] + nums[right]

                    if sums == target:
                        quad = [nums[i], nums[j], nums[left], nums[right]]
                        if quad not in res:
                            res.append(quad)
                        left += 1
                        right -= 1
                    elif sums < target:
                        left += 1
                    else:
                        right -= 1

        return res
