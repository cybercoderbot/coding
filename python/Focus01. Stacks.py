"""
42. Trapping Rain Water
84. Largest Rectangle in Histogram
496. Next Greater Element I
503. Next Greater Element II
856. Score of Parentheses
901. Online Stock Span
907. Sum of Subarray Minimums
1130. Minimum Cost Tree From Leaf Values
"""


class StockSpanner:
    """
    901. Online Stock Span
    We can refer to the same problem 739. Daily Temperatures.

    Push every pair of (price, result) to a stack.
    Pop lower price from the stack and accumulate the count.

    One price will be pushed once and popped once.
    So 2 * N times stack operations and N times calls.
    Time complexity: amortized O(1)
    """

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:

        res = 1
        while self.stack and self.stack[-1][0] <= price:
            p, span = self.stack.pop()
            res += span

        self.stack.append([price, res])

        return res


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        907. Sum of Subarray Minimums
        Define an increasing mono-stack stack which stores the indices of decreasing values. 
        At index i, the sum of minimum of subarrays are res[j] + x * (i-j) once an index j whose value smaller than i has been identified.
        """
        res, stack = [], []
        for i, x in enumerate(arr):

            while stack and arr[stack[-1]] >= x:
                # Increasing mono-stack
                stack.pop()

            if stack:
                j = stack[-1]
                res.append(res[j] + x * (i-j))
            else:
                res.append(x * (i+1))

            stack.append(i)

        return sum(res) % int(1e9 + 7)


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        907. Sum of Subarray Minimums
        """
        res = 0
        stack = []
        for i in range(len(arr)+1):
            while stack and (i == len(arr) or arr[stack[-1]] > arr[i]):
                mid = stack.pop()
                ii = stack[-1] if stack else -1
                res += arr[mid] * (i - mid) * (mid - ii)
            stack.append(i)

        # return res % 1_000_000_007
        return res % int(1e9 + 7)
