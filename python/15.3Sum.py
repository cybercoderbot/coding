# Sort based algorithm

# a+b = -c. 3SUM reduces to 2SUM problem.
# Handling Duplicates in 2SUM

# Say index s and e are forming a solution in a sorted array. Now givens nums[s], there is a unique nums[e] such that nums[s]+nums[e]=Target. Therefore, if nums[s+1] is the same as nums[s], then searching in range s+1 to e will give us a duplicate solution. Thus we must move s till nums[s] != nums[s-1] to avoid getting duplicates.
#                         while s<e and nums[s] == nums[s-1]:
#                             s = s+1
# Handling Duplicates in 3SUM

# Imagine we are at index i and we have invoked the 2SUM problem from index i+1 to end of the array. Now once the 2SUM terminates, we will have a list of all triplets which include nums[i]. To avoid duplicates, we must skip all nums[i] where nums[i] == nums[i-1].
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
# Code

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N, result = len(nums), []

        if N < 3:
            return []

        for i in range(N):
            if i >= 1 and nums[i] == nums[i-1]:
                continue

            target = -1 * nums[i]
            left, right = i+1, N-1

            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return result
