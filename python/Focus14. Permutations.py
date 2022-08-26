class Solution:
    def nextPermutation(self, nums):
        """ 
        31. Next Permutation (in place)
        [1,2,3]->[1,3,2], [1,1,5]->[1,5,1], [3,2,1]->[1,2,3]
        https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
        Time O(N), Space: O(1)
        [0,1,2,5,3,3,0] -> [0,1,3,5,3,2,0] -> [0,1,3,0,2,3,5]
        """
        N = len(nums)
        idx1 = next((i for i in range(N-2, -1, -1)
                     if nums[i] < nums[i+1]), None)
        if idx1 is None:
            nums.reverse()
            # nums.sort()
        else:
            idx2 = next((i for i in range(N - 1, idx1, -1)
                         if nums[i] > nums[idx1]), None)
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
            nums[idx1+1:] = reversed(nums[idx1+1:])
            # nums[idx1 + 1:] = sorted(nums[idx1 + 1:])
        return


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        46. Permutations
        Return all the possible permutations of distinct nums.
        Duplication allowed. 
        [0,1] -> [[0,1],[1,0]]
        Time: O(N!), Space: O(N!)
        """
        @lru_cache(None)
        def backtrack(i):
            """Populate res in backtrack"""
            if i == len(nums):
                res.append(nums.copy())
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        res = []
        backtrack(0)
        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        47. Permutations II
        Duplication NOT allowed.
        [1,1,2] -> [[1,1,2], [1,2,1], [2,1,1]]
        """
        def backtrack(i):
            """Populate res via backtracking."""
            if i == len(nums):
                return res.append(nums.copy())
            seen = set()
            for j in range(i, len(nums)):
                if nums[j] not in seen:
                    nums[i], nums[j] = nums[j], nums[i]
                    backtrack(i+1)
                    nums[i], nums[j] = nums[j], nums[i]
                    seen.add(nums[j])

        res = []
        backtrack(i=0)
        return res


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        60. Permutation Sequence
        Given n and k, return the kth permutation sequence.
        Approach 1 - brute force O(N!)
        """
        if n == 0:
            return ""
        perms = list(permutations(range(1, n+1)))
        return "".join([str(x) for x in perms[k-1]])


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        60. Permutation Sequence
        Given n and k, return the kth permutation sequence.
        """
        res = ""
        nums = list(range(1, n+1))
        k -= 1
        while n:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            res += str(nums.pop(index))
        return res


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        266. Palindrome Permutation
        Return true if a permutation of the s could form a palindrome.
        """
        freq = collections.Counter(s)
        return sum([x & 1 for x in freq.values()]) <= 1


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        """
        267. Palindrome Permutation II
        Return all the palindromic permutations (without duplicates) of s.
        """
        freq = Counter(s)
        odd = sum(x & 1 for x in freq.values())
        if odd > 1:
            return []

        res = []
        vals, mid = [], ""
        for k, v in freq.items():
            vals.extend([k] * (v//2))
            if v & 1:
                mid = k

        def backtrack(i):
            """Permutation without duplicates."""
            if i == len(vals):
                res.append("".join(vals) + mid + "".join(vals[::-1]))

            seen = set()
            for j in range(i, len(vals)):
                if vals[j] not in seen:
                    seen.add(vals[j])
                    vals[i], vals[j] = vals[j], vals[i]
                    backtrack(i+1)
                    vals[i], vals[j] = vals[j], vals[i]

        backtrack(0)
        return res
