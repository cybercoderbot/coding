"""
135. Candy
Hard

There are n children standing in a line. 
Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""


class Solution:
    def candy(self, ratings: List[int]) -> int:

        N = len(ratings)
        if N <= 1:
            return N

        nums = [1] * N
        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                nums[i] = nums[i-1] + 1

        # kids on downwards curve get candies
        # if a kid on both up/down curves (peak or valley)
        # kid gets the maximum candies among the two.
        for i in range(N-1, 0, -1):
            if ratings[i] < ratings[i-1]:
                nums[i-1] = max(nums[i]+1, nums[i-1])

        return sum(nums)
