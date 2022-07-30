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


"""
901. Online Stock Span
Medium

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.

Example 1:
Input:
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output:
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6
"""


class StockSpanner:
    """
    901. Online Stock Span
    We can refer to the same problem 739. Daily Temperatures.

    Push every pair of <price, result> to a stack.
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



"""
907. Sum of Subarray Minimums
Medium

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
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
