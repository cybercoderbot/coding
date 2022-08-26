class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        O(N) Time, O(1) Space
        nums = [1,2,3] -> [1,3,2]
        nums = [3,2,1] -> [1,2,3]
        """
        N = len(nums)
        idx1 = next((i for i in range(N-2, -1, -1)
                     if nums[i] < nums[i+1]), -1)
        if idx1 == -1:
            # [3,2,1] -> [1,2,3]
            nums.reverse()
        else:
            idx2 = next((i for i in range(N-1, idx1, -1)
                         if nums[i] > nums[idx1]), None)
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
            nums[idx1+1:] = reversed(nums[idx1+1:])
        return


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        78. Subsets (no duplicates) (edtsoi430)
        Backtracking: Brute force solution (add or not add)
        """
        def backtrack(idx, sub):
            res.append(sub[:])
            for i in range(idx, len(nums)):
                backtrack(i+1, sub+[nums[i]])
            return

        res = []
        backtrack(idx=0, sub=[])
        return res


class Solution:
    def subsetsWithoutDup(self, nums: List[int]) -> List[List[int]]:
        """
        90. Subsets II (no duplicate subsets)
        Sort nums and compare neighboring values
        """
        res = []
        nums.sort()

        def backtrack(idx, sub):
            res.append(sub[:])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                backtrack(i+1, sub+[nums[i]])
            return

        backtrack(idx=0, sub=[])
        return res


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        39. Combination Sum
        """
        if not nums:
            return []
        nums.sort()
        res = []

        def backtrack(idx, comb, total):
            if total > target:
                return
            if total == target:
                res.append(comb[:])
                return
            for i in range(idx, len(nums)):
                backtrack(i, comb+[nums[i]], total+nums[i])

        backtrack(idx=0, comb=[], total=0)
        return res


class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        """
        40. Combination Sum II (find all unique combinations summing up to target)
        """
        if not nums:
            return []
        nums.sort()
        res = []

        def backtrack(idx, comb, total):
            if total > target:
                return
            if total == target:
                res.append(comb[:])
                return
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                backtrack(i+1, comb + [nums[i]], total + nums[i])

        backtrack(idx=0, comb=[], total=0)
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        46. Permutations
        nums = [1,2,3]
        res = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        """
        res = []

        if len(nums) == 1:
            # nums[:] is a deep copy
            return [nums[:]]

        for i in range(len(nums)):
            x = nums.pop(0)
            perms = self.permute(nums)
            for pm in perms:
                pm.append(x)
            res.extend(perms)
            nums.append(x)

        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        46. Permutations
        47. Permutations II (return all unique permutations)
        nums = [1,2,3]
        res = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        """
        res = []
        freq = Counter(nums)

        def backtrack(freq, perm):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for x in freq:
                if freq[x]:
                    freq[x] -= 1
                    backtrack(freq, perm+[x])
                    freq[x] += 1
            return

        backtrack(freq, [])
        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        47. Permutations II (return all possible unique permutations)
        nums = [1,2,3]
        res = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        """
        res = []
        freq = Counter(nums)

        def backtrack(counter, perm):
            if len(perm) == len(nums):
                res.append(perm)
                return
            for x in freq:
                if freq[x]:
                    freq[x] -= 1
                    backtrack(counter, perm+[x])
                    freq[x] += 1
            return
        backtrack(freq, [])
        return res


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        784. Letter Case Permutation
        s = "a1b2" -> ["a1b2","a1B2","A1b2","A1B2"]
        """
        def backtrack(i, sub):
            if len(sub) == len(s):
                res.append(sub)
                return
            if s[i].isalpha():
                backtrack(sub + s[i].swapcase(), i + 1)
            backtrack(sub + s[i], i + 1)
            return

        res = []
        backtrack(i=0, sub="")
        return res


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        1079. Letter Tile Possibilities
        tiles = "AAB", output = 8
        All possible seqs are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
        """
        res = set()

        @lru_cache(None)
        def dfs(seq, t):
            if seq:
                res.add(seq)
            for i in range(len(t)):
                dfs(seq+t[i], t[:i] + t[i+1:])

        dfs('', tiles)
        return len(res)


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        1079. Letter Tile Possibilities
        tiles = "AAB", output = 8
        All possible seqs are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
        """
        freq = collections.Counter(tiles)

        def dfs():
            res = 0
            for c in freq:
                if not freq[c]:
                    continue
                freq[c] -= 1
                res += dfs() + 1
                freq[c] += 1
            return res

        return dfs()


class Solution:
    def expand(self, s: str) -> List[str]:
        """
        1087. Brace Expansion
        s = "{a,b}c{d,e}f" -> ["acdf","acef","bcdf","bcef"]
        """
        N = len(s)
        res = []

        def dfs(i, sub):
            if i == N:
                res.append(sub)
                return
            if s[i] == "{":
                j = i+1
                while s[j] != "}":
                    j += 1
                options = s[i+1: j].split(",")
                for c in options:
                    dfs(sub + c, j + 1)
            else:
                dfs(sub + s[i], i + 1)

        dfs(i=0, sub="")
        return sorted(res)


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        567. Permutation in String
        Return true if s2 contains a permutation of s1
        Time: O(N * k), Space O(N)
        """
        freq1 = collections.Counter(s1)
        k, N = len(s1), len(s2)
        for i in range(N-k+1):
            freq2 = collections.Counter(s2[i: i+k])
            if freq1 == freq2:
                return True
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        567. Permutation in String
        Return true if s2 contains a permutation of s1
        Time: O(N * logk), Space O(N)
        """
        sort1 = sorted(s1)
        k, N = len(s1), len(s2)
        for i in range(N-k+1):
            sort2 = sorted(s2[i: i+k])
            if sort1 == sort2:
                return True
        return False
