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
