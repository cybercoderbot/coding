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
        freq = Counter()
        # freq = defaultdict(int)
        for right, c in enumerate(s):
            freq[c] += 1
            while freq[c] > 1:
                freq[s[left]] -= 1
                left += 1
            res = max(res, right-left + 1)
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
            res = left = total = 0
            for right, x in enumerate(nums):
                total += x
                while total > k:
                    total -= nums[left]
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
    def balancedString(self, s: str) -> int:
        """
        1234. Replace the Substring for Balanced String
        s = "QWER" -> 0
        s = "QQWE" -> 1
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
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        """
        239. Sliding Window Maximum
        Use a deque to keep indexes of the running maximum num
        Time: O(N), Space: O(N)
        """
        deq = []
        res = []
        for i, x in enumerate(nums):

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while deq and nums[deq[-1]] < x:
                deq.pop(-1)

            deq.append(i)

            # remove indexes of elements out of bound for sliding window
            while deq and i - deq[0] >= k:
                deq.pop(0)

            # sliding window size: k
            if i + 1 >= k:
                res.append(nums[deq[0]])
        return res


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        862. Shortest Subarray with Sum at Least K
        """
        res = inf
        deq = [(-1, 0)]
        total = 0
        for i, x in enumerate(nums):
            total += x
            while deq and total - deq[0][1] >= k:
                start, _ = deq.pop(0)
                res = min(res, i - start)
            while deq and deq[-1][1] >= total:
                deq.pop(-1)
            deq.append((i, total))

        return res if res < inf else -1


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """ 209. Minimum Size Subarray Sum Greater Than k"""
        left = total = 0
        res = len(nums) + 1
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(res, right-left+1)
                total -= nums[left]
                left += 1
        if res == len(nums) + 1:
            return 0
        return res


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        904. Fruit Into Baskets
        1.Problem:
        Start from any index, collect at most 2 types of fruits.
        What is the max amount?
        2.Translation:
        Find out the longest length of subarrays with at most 2 different numbers
        3.Solution:
        Solve with sliding window, and maintain a hashmap counter,
        which count the number of element between the two pointers.
        Time O(N), Space O(1)
        """
        freq = defaultdict(int)
        left = 0
        for right, x in enumerate(fruits):
            freq[x] += 1
            if len(freq) > 2:
                pre = fruits[left]
                freq[pre] -= 1
                if freq[pre] == 0:
                    freq.pop(pre)
                left += 1
        return right - left + 1


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
            res = total = left = 0
            for right in range(len(nums)):
                total += nums[right]
                while total > target:  # sliding window
                    total -= nums[left]
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
