class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        217. Contains Duplicate
        [1,2,3,1] -> true, [1,2,3,4] -> false
        """
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        242. Valid Anagram
        s = "anagram", t = "nagaram" -> True
        """
        seen = defaultdict(int)
        for c in s:
            seen[c] += 1
        for c in t:
            seen[c] -= 1
        return all(x == 0 for x in seen.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        49. Group Anagrams
        ["eat","tea","tan","ate","nat","bat"]
        -> [["bat"],["nat","tan"],["ate","eat","tea"]]
        """
        seen = collections.defaultdict(list)
        for s in strs:
            sort = str(sorted(s))
            seen[sort].append(s)
        return seen.values()


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        347. Top K Frequent Elements
        nums = [1,1,1,2,2,3], k = 2 -> [1,2]
        Bucket sort: map frequency to a list of numbers
        Time: O(N), Space O(N)
        """
        count = defaultdict(int)
        N = len(nums)
        for x in nums:
            count[x] += 1
        freq = [[] for i in range(N + 1)]
        for x, c in count.items():
            freq[c].append(x)

        res = []
        for i in range(N, -1, -1):
            for x in freq[i]:
                res.extend(x)
                if len(res) >= k:
                    return res[:k]


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        692. Top K Frequent Words
        Return the answer sorted by the frequency from highest to lowest. 
        Sort the words with the same frequency by their lexicographical order.
        """
        count = defaultdict(int)
        N = len(words)
        for w in words:
            count[w] += 1
        freq = [[] for i in range(N + 1)]
        for w, c in count.items():
            freq[c].append(w)

        res = []
        for i in range(N, -1, -1):
            for w in sorted(freq[i]):
                res.append(w)
                if len(res) == k:
                    return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        238. Product of Array Except Self
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
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        36. Valid Sudoku
        Time: O(N), Space: O(N) 
        """
        N = 9
        rows = [set() for j in range(N)]
        cols = [set() for j in range(N)]
        boxs = [set() for j in range(N)]

        for i, j in product(range(N), range(N)):
            x = board[i][j]
            k = i//3 * 3 + j//3
            if x == ".":
                continue
            if x in (rows[i] | cols[j] | boxs[k]):
                return False
            rows[i].add(x)
            cols[j].add(x)
            boxs[k].add(x)

        return True


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        128. Longest Consecutive Sequence
        """
        numSet = set(nums)
        longest = 0
        for x in nums:
            # check if its the start of a sequence
            if x - 1 not in numSet:
                length = 1
                while x + length in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
