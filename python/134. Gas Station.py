"""
134. Gas Station
Medium

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

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


class Solution(object):
    def canCompleteCircuit(self, gas, cost):

        if sum(gas) < sum(cost):
            return -1

        res = extra = 0
        for i in range(len(gas)):
            extra += gas[i] - cost[i]
            if extra < 0:
                extra = 0
                res = i + 1

        return res if extra >= 0 else -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """ greedy """
        positive = negative = 0
        res = 0
        for i, (pos, neg) in enumerate(zip(gas, cost)):
            if positive < 0:
                negative += positive
                res = i
                positive = 0
            positive += (pos - neg)

        return res if positive + negative >= 0 else -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_gas = 0
        total = 0
        res = 0
        for idx in range(len(gas)):
            cur_gas += (gas[idx] - cost[idx])
            if cur_gas < 0:
                res = idx + 1
                # Add the negative value of cur_gas to account for the 'visited' gas stations
                total += cur_gas
                cur_gas = 0
        total += cur_gas
        return -1 if total < 0 else res