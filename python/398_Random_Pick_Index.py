class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """

        # If we want to optimize run time then we can use a dictionary to pre-process the nums array.
        # Simply create a map of key (number) and value (list of its indices).
        # Then run reservoir sampling over this input.
        # But the problem statement says that using too much memory is not allowed.
        # In that case, we can iterate the entire array and keep a variable to track the frequency of the target
        # for input into reservoir sampling.
        # Notice random.random() returns uniform random number between [0 to 1]

        count, index = 0, 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                if random.random() <= 1.0/count:
                    index = i
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
