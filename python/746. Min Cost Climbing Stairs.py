"""
746. Min Cost Climbing Stairs
Easy

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6."""


"""
In the forward setup, define total[i] as the total cost of climbing staircase to i,
total[i] = cost[i] + min(total[i-1], total[i-2])
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # The array's length should be 1 longer than the length of cost
        # This is because we can treat the "top floor" as a step to reach

        N = len(cost)
        res = [0] * (N + 1)

        # Start iteration from step 2, since the minimum cost of reaching
        # step 0 and step 1 is 0
        for i in range(2, N + 1):
            cost1 = res[i-1] + cost[i-1]
            cost2 = res[i-2] + cost[i-2]
            res[i] = min(cost1, cost2)

        # The final element in minimum_cost refers to the top floor
        return res[-1]


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        t1 = t2 = 0
        for c in cost:
            t1, t2 = t2, c + min(t1, t2)
        return min(t1, t2)


# bottom-up dp

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f0 = f1 = 0
        for c in reversed(cost):
            f0, f1 = c + min(f0, f1), f0
        return min(f0, f1)


# Adding top-down dp
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @cache
        def dp(i):
            """Return min cost starting from ith stair."""
            if i >= len(cost):
                return 0
            return cost[i] + min(dp(i+1), dp(i+2))

        return min(dp(0), dp(1))
