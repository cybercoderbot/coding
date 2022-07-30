"""
398. Random Pick Index
Medium

Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.
 
Example 1:
Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
"""


class Solution(object):

    def __init__(self, nums: List[int]):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target: int) -> int:
        """
        :type target: int
        :rtype: int
        """

        """
        Reservoir sampling solution.

        If we want to optimize run time then we can use a dictionary to pre-process the nums array.
        Simply create a map of key (number) and value (list of its indices).
        Then run reservoir sampling over this input.
        But the problem statement says that using too much memory is not allowed.
        In that case, we can iterate the entire array and keep a variable to track the frequency of the target
        for input into reservoir sampling.
        Notice random.random() returns uniform random number between [0 to 1]
        
        """
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    res = i
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
