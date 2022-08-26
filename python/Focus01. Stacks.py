class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        84. Largest Rectangle in Histogram
        Use a stack to store non-decreasing height.
        At position i, pop all heights (by index) that is higher than heights[i] from stack.
        Height is obtained from the poped index.
        Width is obtained by index i and last value on stack.
        """

        # non-decreasing mono-stack
        stack = []

        res = 0
        heights.append(0)
        for i, x in enumerate(heights):
            while stack and heights[stack[-1]] > x:
                depth = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                res = max(res, depth * width)
            stack.append(i)

        return res


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        402. Remove K Digits
        Use a mono increasing stack to remove big digits.
        When adding a new digit, check whether the previous is bigger than current  
        and pop it out. In the end, concatenate the remaining elements for the result.
        """
        stack = []
        for x in num:
            while stack and k and stack[-1] > x:
                stack.pop()
                k -= 1
            stack.append(x)

        stack = stack[:-k] if k else stack
        return ''.join(stack).lstrip('0') or '0'


class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        """
        739. Daily Temperatures. Return an array such that answer[i] is 
        the number of days you have to wait to get warmer.
        """
        N = len(nums)
        res = [0] * N
        stack = []

        for i in range(N-1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            res[i] = stack[-1] - i if stack else 0
            stack.append(i)

        return res


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        456. 132 Pattern
        True if i < j < k and nums[i] < nums[k] < nums[j]
        """
        # mono decressing stack
        stack = []
        s3 = -inf
        # reversed 2-3-1 pattern
        for x in reversed(nums):
            if x < s3:
                return True
            while stack and stack[-1] < x:
                s3 = stack.pop()
            stack.append(x)
        return False


class Solution:

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        496. Next Greater Element I
        nums1 = [4,1,2], nums2 = [1,3,4,2] -> [-1,3,-1]
        Time: O(N), Space: O(N), N = num of elements in nums2
        """
        stack = []
        greater = {}
        for x in nums2:
            while stack and x > stack[-1]:
                greater[stack[-1]] = x
                stack.pop()
            stack.append(x)

        # unmatched vals
        for x in stack:
            greater[x] = -1
        return [greater[x] for x in nums1]


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        503. Next Greater Element II (array is circular)
        A typical way to solve circular array problems is to extend the original 
        array to twice length, and the 2nd half has the same element as first half. 
        """
        N = len(nums)
        greater = [-1] * N
        stack = []
        for i, x in enumerate(nums + nums):
            while stack and nums[stack[-1]] < x:
                greater[stack.pop()] = x
            stack.append(i % N)
        return greater


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        581. Shortest Unsorted Continuous Subarray
        """
        pairs = zip(nums, sorted(nums))
        res = [i for i, (x, y) in enumerate(pairs) if x != y]
        return res[-1] - res[0] + 1 if res else 0


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        """
        239. Sliding Window Maximum
        Sliding window minimum/maximum = monotonic increasing/decreasing queue.
        Solution: decreasing mono queue (keep index of max num)
        Time: O(N), Space: O(N)
        """
        res = []
        deq = collections.deque([])
        for i, x in enumerate(nums):
            while deq and i - deq[0] >= k:
                deq.popleft()
            while deq and nums[deq[-1]] < x:
                deq.pop()
            deq.append(i)
            res.append(nums[deq[0]])

        return res[k-1:]


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        918. Maximum Sum Circular Subarray
        Increasing mono-queue
        """
        res, cumsum = -inf, 0
        deq = collections.deque([(-1, 0)])
        for i, x in enumerate(nums + nums):
            cumsum += x
            while deq and i - deq[0][0] > len(nums):
                deq.popleft()
            res = max(res, cumsum - deq[0][1])
            while deq and deq[-1][1] >= cumsum:
                deq.pop()
            deq.append((i, cumsum))
        return res


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        503. Next Greater Element II (array is circular)
        Use the stack to record the reversed array nums. Loop the array from last integer to the first one. If the last integer in stack is bigger than the current interger in array, we have found the answer. Otherwise, we need to keep pop up the integer in stack. Besides, we need to push the current integer to the stack in each step.
        """
        N = len(nums)
        res = [-1] * N
        stack = nums[::-1]
        for i in range(N-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
        return res


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        856. Score of Parentheses
        s = "()" -> 1, s = "(())" -> 2, s = "()()" -> 2
        res record the score at the current layer level.

        If we meet '(',
        we push the current score to stack, enter the next inner layer level,
        and reset res = 0.

        If we meet ')',
        the res score will be doubled and will be at least 1.
        We exit the current layer level, and set res += stack.pop() + res

        Complexity: O(N) time and O(N) space
        """

        stack, res = [], 0
        for c in s:
            if c == '(':
                stack.append(res)
                res = 0
            else:
                new = stack.pop() + max(res, 1)
                res += new
        return res


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        2104. Sum of Subarray Ranges
        Time: O(N^2), Space O(1)
        """
        res = 0
        N = len(nums)
        for i in range(N):
            low = high = nums[i]
            for j in range(i, N):
                low = min(low, nums[j])
                high = max(high, nums[j])
                res += high - low
        return res


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
    def sumSubarrayMins(self, nums: List[int]) -> int:
        """
        907. Sum of Subarray Minimums
        Define an increasing mono-stack stack which stores the indices of decreasing values. 
        At index i, the sum of minimum of subarrays are res[j] + x * (i-j) once an index j 
        whose value smaller than i has been identified.
        """
        res, stack = [], []
        for right, x in enumerate(nums):
            while stack and nums[stack[-1]] >= x:
                stack.pop()
            if stack:
                left = stack[-1]
                res.append(res[left] + x * (right-left))
            else:
                res.append(x * (right+1))
            stack.append(right)

        return sum(res) % int(1e9 + 7)


class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        """
        907. Sum of Subarray Minimums
        """
        res = 0
        stack = []
        for i in range(len(nums)+1):
            while stack and (i == len(nums) or nums[stack[-1]] > nums[i]):
                mid = stack.pop()
                ii = stack[-1] if stack else -1
                res += nums[mid] * (i - mid) * (mid - ii)
            stack.append(i)
        return res % int(1e9 + 7)


class Solution:
    def mctFromLeafValues(self, nums: List[int]) -> int:
        """
        1130. Minimum Cost Tree From Leaf Values
        """
        res = 0
        stack = [inf]

        for x in nums:
            while stack[-1] <= x:
                mid = stack.pop()
                res += mid * min(stack[-1], x)
            stack.append(x)

        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
