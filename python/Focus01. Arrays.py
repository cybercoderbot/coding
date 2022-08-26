class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        4. Median of Two Sorted Arrays
        """
        nums = sorted(nums1 + nums2)
        N = len(nums)
        mid = int(N/2)
        if N % 2:
            return nums[mid]
        else:
            return (nums[mid-1] + nums[mid]) / 2


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        33. Search in Rotated Sorted Array
        nums = [4,5,6,7,0,1,2], target = 0 -> 4
        """
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        81. Search in Rotated Sorted Array II
        nums = [2,5,6,0,0,1,2], target = 0 ->  true
        """
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        349. Intersection of Two Arrays
        """
        return list(set(nums1) & set(nums2))


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        88. Merge Sorted Array
        # Add the elements of num2 into the end of nums1 (starting from m).
        """
        for i in range(n):
            nums1[i + m] = nums2[i]
        nums1.sort()
        return


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        283. Move Zeroes (in place)
        [0,1,0,3,12] -> [1,3,12,0,0]
        """
        j = 0
        for i, x in enumerate(nums):
            if x != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        189. Rotate Array (in place)
        """
        N = len(nums)
        rotated = [0] * N
        for i in range(N):
            rotated[(i+k) % N] = nums[i]
        nums[:] = rotated
        return


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        268. Missing Number
        """
        return sum(range(len(nums)+1)) - sum(nums)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        268. Missing Number
        """
        N = len(nums)
        return int(N*(N+1)/2) - sum(nums)


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        280. Wiggle Sort (in place)
        nums[0] <= nums[1] >= nums[2] <= nums[3]....
        [3,5,2,1,6,4] -> [3,5,1,6,2,4]
        """
        for i in range(len(nums)):
            nums[i:i+2] = sorted(nums[i:i+2], reverse=i & 1)
        return


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        324. Wiggle Sort II (in place)
        nums[0] < nums[1] > nums[2] < nums[3]....
        [1,5,1,1,6,4] -> [1,6,1,5,1,4]
        """
        nums.sort()
        N = len(nums[::2])
        small, large = nums[:N], nums[N:]
        nums[::2], nums[1::2] = small[::-1], large[::-1]
        return


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        724. Find Pivot Index
        nums = [1,7,3,6,5,6] -> 3 (1+7+3 = 5+6 = 11)
        """
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        238. Product of Array Except Self
        nums = [1,2,3,4] -> [24,12,8,6]
        nums = [-1,1,0,-3,3] -> [0,0,9,0,0]
        """
        N = len(nums)
        res = [1] * N
        prefix = 1
        for i in range(N):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(N-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        896. Monotonic Array
        True if the given array is monotonic (increasing or decreasing)
        """
        increase = all(x <= y for x, y in zip(nums[:-1], nums[1:]))
        decrease = all(x >= y for x, y in zip(nums[:-1], nums[1:]))
        return increase or decrease


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        1470. Shuffle the Array
        [x1,x2,...,xn,y1,y2,...,yn] -> [x1,y1,x2,y2,...,xn,yn]
        """
        res = []
        for x, y in zip(nums[:n], nums[n:]):
            res.extend([x, y])
        return res


class Solution:
    def validMountainArray(self, nums: List[int]) -> bool:
        """
        941. Valid Mountain Array
        """
        left, right = 0, len(nums)-1
        while left < right and nums[left] < nums[left+1]:
            left += 1
        while left < right and nums[right-1] > nums[right]:
            right -= 1
        return 0 < left and left == right and right < len(nums)-1


class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        """
        852. Peak Index in a Mountain Array
        """
        left, right = 0, len(nums)-1
        while left < right-1:
            mid = (left+right)//2
            if nums[mid-1] < nums[mid]:
                left = mid
            elif nums[mid-1] > nums[mid]:
                right = mid
        return left


class Solution:
    def arrayRankTransform(self, nums: List[int]) -> List[int]:
        """
        1331. Rank Transform of an Array
        [40,10,20,30] -> [4,1,2,3], [3,3,3] -> [1,1,1]
        """
        sort = sorted(set(nums))
        rank = defaultdict(int)
        for i, x in enumerate(sort, 1):
            if x not in rank:
                rank[x] = i
        for i, x in enumerate(nums):
            nums[i] = rank[x]
        return nums


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        1636. Sort Array by Increasing Frequency
        [1,1,2,2,2,3] -> [3,1,1,2,2,2]
        """
        freq = collections.Counter(nums)
        nums.sort(reverse=True)
        nums.sort(key=lambda x: freq[x])
        return nums


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        540. Single Element in a Sorted Array
        """
        return next(k for k, v in Counter(nums).items() if v == 1)


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        540. Single Element in a Sorted Array
        Solution: pairwise comparison
        """
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """
        1822. Sign of the Product of an Array
        """
        count = 0
        for x in nums:
            if x == 0:
                return 0
            if x < 0:
                count += 1
        return -1 if count % 2 else 1


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        2149. Rearrange Array Elements by Sign
        [3,1,-2,-5,2,-4] -> [3,-2,1,-5,2,-4]
        """
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        res = []
        for x, y in zip(pos, neg):
            res.extend([x, y])
        return res


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        525. Contiguous Array. Return the max length of a contiguous subarray 
        with an equal number of 0 and 1.
        """
        res = 0
        seen = {}
        c = 0
        for i, x in enumerate(nums):
            c += [-1, 1][x]
            if c == 0:
                res = i + 1
            if c in seen:
                res = max(res, i-seen[c])
            else:
                seen[c] = i
        return res


class Solution(object):
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        581. Shortest Unsorted Continuous Subarray
        Return the length of shortest subarray such that if you sort this subarray,
        the entire array is sorted
        """
        pairs = zip(nums, sorted(nums))
        res = [i for i, (x, y) in enumerate(pairs) if x != y]
        return res[-1] - res[0] + 1 if res else 0


class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparse = {}
        for i, x in enumerate(nums):
            if x:
                self.sparse[i] = x

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        1570. Dot Product of Two Sparse Vectors
        """
        res = 0
        for i, x in self.sparse.items():
            if i in vec.sparse:
                res += x * vec.sparse[i]
        return res
