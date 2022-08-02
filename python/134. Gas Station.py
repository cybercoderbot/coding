"""
134. Gas Station
Medium

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i]. You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i+1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        If car starts at A and can not reach B. Any station between A and B
        can not reach B.(B is the first station that A can not reach.)
        1) If sum of gas is more than sum of cost, then there must be a solution. And the question guaranteed that the solution is unique (The first one I found is the right one).
        2) The tank should never be negative, so restart whenever there is a negative number.
        Time: O(N), Space: O(1). Two passes
        """

        # 1) determine if we have a solution
        if len(gas) != len(cost) or sum(gas) < sum(cost):
            return -1

        # 2) find out where to start
        res = tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0     # reset tank
                res = i + 1  # update the stating gas station

        return res if tank >= 0 else -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if len(gas) != len(cost) or sum(gas) < sum(cost):
            return -1

        tank = needed = start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                needed -= tank
                start = i + 1
                tank = 0
        return start if tank >= needed else -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, total_surplus, surplus, start = len(gas), 0, 0, 0

        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """ greedy """
        pos = neg = 0
        res = 0
        for i, (x, y) in enumerate(zip(gas, cost)):
            if pos < 0:
                neg += pos
                res = i
                pos = 0
            pos += (x - y)

        return res if pos + neg >= 0 else -1
