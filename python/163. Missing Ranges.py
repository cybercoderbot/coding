"""
163. Missing Ranges
Easy

You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Example 1:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"

Example 2:
Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.
"""


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """
        nums = [0,1,3,50,75], lower = 0, upper = 99
        Output: ["2","4->49","51->74","76->99"]
        """

        # [-1,0,1,3,50,75,100]
        nums = [lower-1] + nums + [upper+1]
        res = []

        for pre, cur in zip(nums[:-1], nums[1:]):
           if cur - pre == 2:
                res.append(str(pre+1))
            elif cur - pre > 2:
                res.append(str(pre+1)+'->'+str(cur-1))

        return res



class Solution:

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        nums.append(upper+1)
        pre = lower - 1
        res = []

        for x in nums:
            if x == pre + 2:
                res.append(str(x-1))
            elif x > pre + 2:
                res.append(str(pre + 1) + "->" + str(x - 1))
            pre = x
        return res


