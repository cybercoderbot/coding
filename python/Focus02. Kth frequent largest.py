class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        414. Third Maximum Number
        [2,2,3,1] -> 1
        """
        vals = set(nums)
        if len(vals) < 3:
            return max(vals)
        vals.remove(max(vals))
        vals.remove(max(vals))
        return max(vals)


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        414. Third Maximum Number
        """
        first, second, third = -inf, -inf, -inf
        for x in nums:
            if x in (first, second, third):
                continue
            if x > third:
                third = x
            if third > second:
                third, second = second, third
            if second > first:
                second, first = first, second
        return third if third > -inf else first


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        402. Remove K Digits (mono increasing stack)
        Return the smallest integer after removing k digits.
        num = "1432219", k = 3 -> "1219"
        In order to get the smallest number, we have to get rid of as many as big digits. 
        We can use a mono increasing stack to help us remove those big digits. When adding 
        a new digit, we check whether the previous is bigger than the current. If yes, pop 
        it out. In the end, we concatenate the remaining digits from the stack and return 
        the result.
        """
        stack = []
        for x in num:
            while k and stack and x < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(x)

        stack = stack[:-k] if k else stack
        return ''.join(stack).lstrip('0') or '0'


class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        """
        414. Third Maximum Number
        Assume the final result is N,
        And there are m number not missing in the range of [1, N].
        Binary search the m in range [0, len(nums)].

        If there are m number not missing,
        that is nums[0], nums[1] .. nums[m-1],
        the number of missing under nums[m] is nums[m] - 1 - m.

        If nums[m] - 1 - m < k, m is too small, we update left = m.
        If nums[m] - 1 - m >= k, m is big enough, we update right = m.

        Note that, we exit the while loop, left = r,
        which equals to the number of missing number used.
        So the Kth positive number will be left + k.
        Time O(logN), Space O(1)
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] - mid <= k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        215. Kth Largest Element in an Array (Min Heap) 
        heap.pop(): pop the smallest item (heap[0])
        Maintain a min heap of k values. The kth largest is the heap's root 
        after all elements have been processed.
        First number in the k-length heap is the k-th largest number
        O(NlogK) Time, O(N) space
        """
        heap = nums[:]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return heap[0]


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        """
        1985. Find the Kth Largest Integer in the Array
        """
        heap = []
        for x in nums:
            heappush(heap, int(x))
            if len(heap) > k:
                heappop(heap)
        return str(heap[0])


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        215. Kth Largest Element in an Array (Min Heap) 
        Time: O(k + (N-k) log k), space: O(k)
        """
        heap = nums[:k]
        heapq.heapify(heap)
        for x in nums[k:]:
            if x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap[0]


class Solution:
    @lru_cache(None)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        215. Kth Largest Element in an Array (Quick Select)
        Average time O(N), Space O(N)
        """
        if not nums:
            return

        pivot = random.choice(nums)
        large = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        small = [x for x in nums if x < pivot]

        L, M = len(large), len(mid)
        if k <= L:
            return self.findKthLargest(large, k)
        elif k > L + M:
            return self.findKthLargest(small, k - L - M)
        else:
            return mid[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Hoare's selection algo"""

        def partition(left, right):
            """
            Partition nums[left:right+1] into two parts
            """
            x = randint(left, right)
            nums[right], nums[x] = nums[x], nums[right]
            i = left
            while i < right:
                if nums[i] < nums[right]:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
                i += 1
            nums[left], nums[right] = nums[right], nums[left]
            return left

        left, right = 0, len(nums)
        while left < right:
            mid = partition(left, right-1)
            if mid + k == len(nums):
                return nums[mid]
            elif mid + k > len(nums):
                right = mid
            else:
                left = mid + 1


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        703. Kth Largest Element in a Stream (Min Heap)
        """
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        215. Kth Largest Element in an Array (Min Heap)
        Use min heap to keep up to k smallest elements of the nums.
        Then top of the min heap is the kth largest element.
        Time: O(NlogK), Space: O(K)
        """
        heap = []
        for x in nums:
            heappush(heap, x)
            if len(heap) > k:
                heappop(heap)
        return heap[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        215. Kth Largest Element in an Array (Max Heap)
        Time: O(N + KlogN), heapify cost O(N), heappop k times costs O(KlogN)
        Space: O(N)
        """
        heap = [-x for x in nums]
        heapify(heap)
        for i in range(k-1):
            heappop(heap)
        return -heap[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        215. Kth Largest Element in an Array (quick select)
        O(N) ~ O(N^2) Time, O(1) space
        """
        return heapq.nlargest(k, nums)[-1]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        215. Kth Largest Element in an Array
        Init a heap the smallest element first, and add all elements into heap 
        one by one, keeping the size of the heap <= k.
        O(Nlogk) time, O(k) space
        """
        return heapq.nlargest(k, nums)[-1]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        215. Kth Largest Element in an Array (must O(N) time)
        O(NlogN) Time, O(1) Space
        """
        return sorted(nums)[-k]
