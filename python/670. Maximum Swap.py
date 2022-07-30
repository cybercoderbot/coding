"""
670. Maximum Swap
Medium

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.
"""


"""
Approach:

Find the max of given array of digits.
If max matches with the first digit (index 0) then there is no benefit of swapping, so recursively solve for remaining array i.e. index 1 onwards
Else if - digit at index 0 is not equal to max of that array then swap it with the last occurance of max in the given array.
"""


def solve(nums):
    if not nums:
        return nums

    MAX = max(nums)
    if nums[0] == MAX:
        return [nums[0]] + solve(nums[1:])
    else:
        index = nums[::-1].index(MAX)
        nums[0], nums[-(index+1)] = nums[-(index+1)], nums[0]
        return nums


class Solution:
    def maximumSwap(self, num: int) -> int:

        nums = [int(x) for x in str(num)]
        swapped = solve(nums)

        return int(''.join(str(x) for x in swapped))
