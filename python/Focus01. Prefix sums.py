
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        238. Product of Array Except Self
        """
        N = len(nums)
        res = [1] * N

        left = 1
        for i in range(N):
            res[i] = left
            left *= nums[i]

        right = 1
        for i in range(N-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        238. Product of Array Except Self
        """
        N = len(nums)
        res = [1] * N

        left, right = 1, 1
        for i in range(N):
            res[i] *= left
            res[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        238. Product of Array Except Self
        """
        N = len(nums)
        res = [1] * N
        for i in range(1, N):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for i in range(N-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res


"""
+-----+-+-------+     +--------+-----+     +-----+---------+     +-----+--------+
|     | |       |     |        |     |     |     |         |     |     |        |
|     | |       |     |        |     |     |     |         |     |     |        |
+-----+-+       |     +--------+     |     |     |         |     +-----+        |
|     | |       |  =  |              |  +  |     |         |  -  |              |
+-----+-+       |     |              |     +-----+         |     |              |
|               |     |              |     |               |     |              |
|               |     |              |     |               |     |              |
+---------------+     +--------------+     +---------------+     +--------------+

   sums[i][j]    =    sums[i-1][j]    +     sums[i][j-1]    -   sums[i-1][j-1]  +  matrix[i-1][j-1]

+---------------+   +---------+----+   +---+-----------+   +---------+----+   +---+----------+
|               |   |         |    |   |   |           |   |         |    |   |   |          |
|   (r1,c1)     |   |         |    |   |   |           |   |         |    |   |   |          |
|   +------+    |   |         |    |   |   |           |   +---------+    |   +---+          |
|   |      |    | = |         |    | - |   |           | - |      (r1,c2) | + |   (r1,c1)    |
|   |      |    |   |         |    |   |   |           |   |              |   |              |
|   +------+    |   +---------+    |   +---+           |   |              |   |              |
|        (r2,c2)|   |       (r2,c2)|   |   (r2,c1)     |   |              |   |              |
+---------------+   +--------------+   +---------------+   +--------------+   +--------------+
"""


class NumArray:
    def __init__(self, nums: List[int]):
        self.cumsum = nums.copy()
        for i in range(1, len(nums)):
            self.cumsum[i] += self.cumsum[i-1]

    def sumRange(self, left: int, right: int) -> int:
        """
        303. Range Sum Query - Immutable
        """
        if left == 0:
            return self.cumsum[right]
        return self.cumsum[right] - self.cumsum[left-1]


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        M, N = len(matrix), len(matrix[0])
        self.cumsum = [[0]*(N+1) for _ in range(M+1)]
        for i, j in product(range(M), range(N)):
            self.cumsum[i+1][j+1] = matrix[i][j] + self.cumsum[i][j+1] \
                + self.cumsum[i+1][j] - self.cumsum[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        304. Range Sum Query 2D - Immutable
        Calculate the sum of the elements of matrix inside the rectangle defined 
        by its upper left corner (row1, col1) and lower right corner (row2, col2)
        """
        x22 = self.cumsum[row2+1][col2+1]
        x11 = self.cumsum[row1][col1]
        x12 = self.cumsum[row1][col2+1]
        x21 = self.cumsum[row2+1][col1]
        return x22 - x12 - x21 + x11


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        523. Continuous Subarray Sum
        Return true if nums has a continuous subarray of size at least two 
        whose elements sum up to a multiple of k, or false otherwise.
        Idea: if sum(nums[i:j]) % k == 0, then sum(nums[:j]) % k == sum(nums[:i]) % k. So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i. Once some later sum(nums[:i']) % k == sum(nums[:i]) % k and i' - i > 1, we return True.
        Trick: -1 is just before you start the index. So if you get the first 2 elements sum to k, your current i is 1 (first occurrence, not seen before). So 1 - (-1) = 2 still satisfies the return True condition. This is very clever though.
        cumsum calculate the prefix sum remainder of input array nums
        seen will record the first occurrence of the remainder.
        If we see the same remainder before, it means the subarray sum is a multiple of k
        """
        seen = defaultdict(int, {0: -1})
        cumsum = 0
        for i, x in enumerate(nums):
            cumsum += x
            cumsum %= k
            if cumsum not in seen:
                seen[cumsum] = i
            elif i - seen[cumsum] >= 2:
                return True
        return False


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        560. Subarray Sum Equals K
        Return the total number of subarrays whose sum equals to k.
        Brute force. O(N^2) Time
        """
        res = 0
        N = len(nums)
        for i in range(N):
            cumsum = nums[i]
            if cumsum == k:
                res += 1
            for j in range(i+1, N):
                cumsum += nums[j]
                if cumsum == k:
                    res += 1
        return res


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        560. Subarray Sum Equals K
        Return the total number of subarrays whose sum equals to k.
        To compute range sum nums[i:j], we can use sum[j+1]-sum[i].
        """
        freq = defaultdict(int)
        res, cumsum = 0, 0
        for x in [0] + nums:
            cumsum += x
            res += freq[cumsum-k]
            freq[cumsum] += 1
        return res


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        560. Subarray Sum Equals K
        Return the total number of subarrays whose sum equals to k.
        To compute range sum nums[i:j], we can use sum[j+1]-sum[i].
        """
        res, cumsum = 0, 0
        freq = defaultdict(int, {0: 1})
        for x in nums:
            cumsum += x
            res += freq[cumsum-k]
            freq[cumsum] += 1
        return res


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

        Basic idea,  at every nums[i], find the shortest j that nums[i:j-1] >= k.
        Solution, for csum[i], find the smallest j that csum[j] - csum[i] >= k.

        https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
        discuss/143726/C%2B%2BJavaPython-O(N)-Using-Deque
        """
        deq = collections.deque([(-1, 0)])
        csum, res = 0, inf
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
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        974. Subarray Sums Divisible by k
        Define cumsum modumo k and maintain a frequency table.
        """
        freq = defaultdict(int, {0: 1})
        res, cumsum = 0, 0
        for x in nums:
            cumsum = (cumsum + x) % k
            res += freq[cumsum]
            freq[cumsum] += 1
        return res


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        1074. Number of Submatrices That Sum to Target
        Return the number of non-empty submatrices that sum to target.
        """
        res = 0
        M, N = len(matrix), len(matrix[0])
        cumsum = [[0]*(N+1) for _ in range(M+1)]

        for i, j in product(range(M), range(N)):
            cumsum[i+1][j+1] = matrix[i][j] + \
                cumsum[i+1][j] + cumsum[i][j+1] - cumsum[i][j]

            for k in range(i+1):
                freq = {0: 1}
                for j in range(N):
                    diff = cumsum[i+1][j+1] - cumsum[k][j+1]
                    res += freq.get(diff - target, 0)
                    freq[diff] = 1 + freq.get(diff, 0)
        return res
