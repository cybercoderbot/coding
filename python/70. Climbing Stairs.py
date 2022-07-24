"""
70. Climbing Stairs
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


"""
Same simple algorithm written in every offered language. Variable a tells you the number of ways to reach the current step, and b tells you the number of ways to reach the next step. So for the situation one step further up, the old b becomes the new a, and the new b is the old a+b, since that new step can be reached by climbing 1 step from what b represented or 2 steps from what a represented.

Ruby wins, and "the C languages" all look the same.
"""


def climbStairs(self, n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
