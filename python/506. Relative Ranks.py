"""
506. Relative Ranks
Easy

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

Example 1:
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Example 2:
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
"""


class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        """
        Step1: Initialize a list and assign the total ranks
        Step2: Using a dictionary map the score with respective rank 
        Final: Return the ranks using the input score list order
        Time: O(NlogN)
        """
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        sorts = sorted(scores, reverse=True)
        for i in range(4, len(scores)+1):
            ranks.append(str(i))

        d = {}
        for s, r in zip(sorts, ranks):
            d[s] = r
        return [d[i] for i in scores]


class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        # Sort scores from best to worst
        nums_sorted = sorted(scores, reverse=True)

        # Map each sorted score to its index
        s = {score: index for index, score in enumerate(nums_sorted)}

        # Create list of medals in ascending order
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"] + \
            [str(i) for i in range(4, len(scores) + 1)]

        # Generate the list of medals in order
        res = [medals[s[n]] for n in scores]
        return res


class Solution:
    def findRelativeRanks(self, nums):
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + \
            map(str, range(4, len(nums) + 1))
        return map(dict(zip(sort, rank)).get, nums)


class Solution:
    def findRelativeRanks(self, nums):
        dunums = sorted(nums, reverse=True)
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"] + \
            [str(i + 1) for i in range(3, len(nums))]
        dt = dict(zip(dunums, medal))
        return [dt[i] for i in nums]


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        nums_sorted = sorted(nums, reverse=True)
        awards = ["Gold Medal", "Silver Medal", "Bronze Medal"] + \
            [str(i) for i in range(4, len(nums) + 1)]
        num_to_award = {num: award for num, award in zip(nums_sorted, awards)}
        return [num_to_award[num] for num in nums]
