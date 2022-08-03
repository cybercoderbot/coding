class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        46. Permutations
        Return all the possible permutations of distinct nums.
        Duplication allowed. 
        [0,1] -> [[0,1],[1,0]]

        Time: O(N!), Space: O(N!)
        """

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

        nodd = sum(x & 1 for x in freq.values())
        if nodd > 1:
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
