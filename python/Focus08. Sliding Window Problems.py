"""
Sliding Window Problems

How do we recognize a sliding window problem? Well, there are three things to look for:

1. A question asking you to analyze a contiguous set of data (subarray, substring, etc)
2. A predefined condition that can be analyzed for each set of data
3. The max, min, longest, shortest, number of, etc things that meet the condition.

You can use the same sliding window algorithms with a couple different variations for almost every sliding window problem. This particular problem requires the use of a dynamically resizing sliding window (one that gets longer until it meets the condition and shrinks until it does not). I left comments for every piece of the code. It's a bit longer than the "concise" answers but I prefer a longer, more readable piece of code over a short and unreadable one. You could have also used an array to store the character frequencies but I like the hashmap implementation better in terms of readability.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        3. Longest Substring Without Repeating Characters
        """
        res = left = 0
        freq = collections.Counter()
        for right, c in enumerate(s):
            freq[c] += 1
            while freq[c] > 1:
                freq[s[left]] -= 1
                left += 1
            res = max(res, right-left + 1)
        return res


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        121. Best Time to Buy and Sell Stock
        """
        res = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
            res = max(res, prices[right] - prices[left])
        return res


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        """
        239. Sliding Window Maximum
        Time: O(Nk), where N is number of elements in the array.
        Space: O(N−k+1) for an output array.
        TLE
        """
        N = len(nums)
        if N * k == 0:
            return []
        return [max(nums[i:i + k]) for i in range(N - k + 1)]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        239. Sliding Window Maximum
        Sliding window minimum/maximum = monotonic increasing/decreasing queue.
        Solution: decreasing mono queue (keep index of max num)
        It has following properties:
        1) Elements in deque are always in decreasing order.
        2) They are always elements from last sliding window of k elements.
        3) It follows from here, that biggest element in current sliding window will 
           be the 0-th element in it.
        Time: O(N), Space: O(N)
        """
        deq, res = collections.deque([]), []
        for i, x in enumerate(nums):
            while deq and i - deq[0] >= k:
                deq.popleft()
            while deq and nums[deq[-1]] < x:
                deq.pop()
            deq.append(i)
            res.append(nums[deq[0]])
        return res[k-1:]


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        862. Shortest Subarray with Sum at Least k
        Use a deque to keep track of (i, cumsum)
        Calculate prefix sum of nums.
        csum[j] - csum[i] represents the sum of subarray nums[i:j-1]
        Deque deq will keep indexes of increasing csum[i].
        For every csum[i], we will compare csum[i] - csum[deq[0]] with k.
        Every index will be: pushed exactly once, popped at most once.

        Basic idea, at every nums[i], find the shortest j that nums[i:j-1] >= k.
        Solution, for csum[i], find the smallest j that csum[j] - csum[i] >= k.

        https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
        discuss/143726/C%2B%2BJavaPython-O(N)-Using-Deque
        """
        csum, res = 0, inf
        deq = collections.deque([(-1, 0)])
        for i, x in enumerate(nums):
            csum += x
            while deq and csum - deq[0][1] >= k:
                start, sm = deq.popleft()
                res = min(res, i - start)
            while deq and deq[-1][1] >= csum:
                deq.pop()
            deq.append((i, csum))
        return res if res < inf else -1


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        480. Sliding Window Median
        sortedList add: O(logk), remove: O(logk) 
        """
        from sortedcontainers import SortedList
        window = SortedList()
        res = []
        for i in range(len(nums)):
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i-k])
            if len(window) == k:
                if k % 2:
                    median = window[k//2]
                else:
                    median = (window[k//2-1] + window[k//2]) / 2
                res.append(median)
        return res


class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        """
        930. Binary Subarrays With Sum
        Return the number of non-empty subarrays with a sum k
        """
        freq = collections.Counter({0: 1})
        csum = res = 0
        for x in nums:
            csum += x
            res += freq[csum-k]
            freq[csum] += 1
        return res


class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        """
        930. Binary Subarrays With Sum
        Return the number of non-empty subarrays with a sum k
        """
        def atMost(k):
            if k < 0:
                return 0
            res = left = cumsum = 0
            for right, x in enumerate(nums):
                cumsum += x
                while cumsum > k:
                    cumsum -= nums[left]
                    left += 1
                res += right - left + 1
            return res

        return atMost(k) - atMost(k-1)


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        992. Subarrays with k Different Integers
        """
        def atMost(k):
            freq = collections.Counter()
            res = left = diff = 0
            for right, x in enumerate(nums):
                diff += (freq[x] == 0)
                freq[x] += 1
                while diff > k:
                    freq[nums[left]] -= 1
                    diff -= (freq[nums[left]] == 0)
                    left += 1
                res += right - left + 1
            return res

        return atMost(k) - atMost(k-1)


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        1358. Number of ALL Substrings Containing 3 Characters
        """
        freq = {x: 0 for x in 'abc'}
        res = left = 0
        for right, c in enumerate(s):
            freq[c] += 1
            while all(freq.values()):
                freq[s[left]] -= 1
                left += 1
            res += left
        return res


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        918. Maximum Sum Circular Subarray
        Increasing mono-queue
        """
        res, cumsum = -inf, 0
        deq = collections.deque([(-1, 0)])
        for i, x in enumerate(nums + nums):
            if i - deq[0][0] > len(nums):
                deq.popleft()
            cumsum += x
            res = max(res, cumsum - deq[0][1])
            while deq and deq[-1][1] >= cumsum:
                deq.pop()

            deq.append((i, cumsum))
        return res


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        904. Fruit Into Baskets
        max 2 types of element in the current sliding window. 
        And you could pick any element in specified index just once.
        Time O(N), Space O(1)
        """
        freq = collections.Counter()
        left, res = 0, 0
        for right, x in enumerate(fruits):
            freq[x] += 1
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if not freq[fruits[left]]:
                    freq.pop(fruits[left])
                left += 1
            res = max(res, right - left + 1)
        return res


class Solution:
    def balancedString(self, s: str) -> int:
        """
        1234. Replace the Substring for Balanced String
        s = "QWER" -> 0, s = "QQWE" -> 1
        Time: O(N), Space: O(N)
        """
        freq = collections.Counter(s)
        res = N = len(s)
        left = 0
        for right, c in enumerate(s):
            freq[c] -= 1
            while left < N and all(freq[c] <= N/4 for c in 'QWER'):
                res = min(res, right - left + 1)
                freq[s[left]] += 1
                left += 1
        return res


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        862. Shortest Subarray with Sum at Least K
        Use a mono increasing deque to keep track of (i, cumsum)

        """
        res = inf
        deq = collections.deque([(-1, 0)])
        cumsum = 0
        for i, x in enumerate(nums):
            cumsum += x
            while deq and cumsum - deq[0][1] >= k:
                res = min(res, i - deq.popleft()[0])
            while deq and deq[-1][1] >= cumsum:
                deq.pop()
            deq.append((i, cumsum))

        return res if res < inf else -1


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """ 
        209. Minimum Size Subarray Sum Greater Than k
        target = 7, nums = [2,3,1,2,4,3] -> output: 2
        """
        left = cumsum = 0
        res = len(nums) + 1
        for right in range(len(nums)):
            cumsum += nums[right]
            while cumsum >= target:
                res = min(res, right-left+1)
                cumsum -= nums[left]
                left += 1
        if res == len(nums) + 1:
            return 0
        return res


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        485. Max Consecutive Ones I
        Return the max number of consecutive 1's
        """
        res = count = 0
        for x in nums:
            if x:
                count += 1
            else:
                count = 0
            res = max(res, count)
        return res


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        487. Max Consecutive Ones II
        Return the max number of consecutive 1's if you can flip at most one 0
        """
        zeros, left = 0, 0
        res = 0
        for right, x in enumerate(nums):
            zeros += (x == 0)
            while zeros > 1:
                zeros -= (nums[left] == 0)
                left += 1
            res = max(res, right - left + 1)
        return res


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        1004. Max Consecutive Ones III
        Return max number of consecutive 1's if you can flip at most k 0's
        """
        zeros, left = 0, 0
        res = 0
        for right, x in enumerate(nums):
            zeros += (x == 0)
            if zeros > k:
                zeros -= (nums[left] == 0)
                left += 1
                res = max(res, right - left + 1)
        return res


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        1248. Count Number of Nice Subarrays
        Nice subarray: it has exactly k odd numbers in it
        """
        def atMost(k):
            res = left = 0
            odd = 0
            for right in range(len(nums)):
                odd += nums[right] % 2
                while odd > k:
                    odd -= nums[left] % 2
                    left += 1
                res += right - left + 1
            return res

        return atMost(k)-atMost(k-1)


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        1248. Count Number of Nice Subarrays
        Nice subarray: it has exactly k odd numbers in it
        """
        seen = defaultdict(int)
        seen[0] = 1
        odd = res = 0
        for x in nums:
            odd += x % 2
            seen[odd] += 1
            if odd-k in seen:
                res += seen[odd-k]
        return res


class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        """
        1918. Kth Smallest Subarray Sum
        """
        def nsubs(target):
            """Return num of subarrays whose sums <= target """
            res = cumsum = left = 0
            for right in range(len(nums)):
                cumsum += nums[right]
                while cumsum > target:  # sliding window
                    cumsum -= nums[left]
                    left += 1
                res += right - left + 1
            return res

        low, high = 0, sum(nums)
        while low < high:
            mid = (low + high) // 2
            if nsubs(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low
