class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    167. Two Sum II - Input Array Is Sorted
    """

    left, right = 0, len(nums)-1

     while left < right:
          sums = nums[left] + nums[right]

           if sums == target:
                return [left+1, right+1]
            if sums < target:
                left += 1
            else:
                right -= 1
