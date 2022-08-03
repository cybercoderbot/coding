class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. 2Sum. Use hashmap to store seen (x, i) pair 
        """
        seen = defaultdict(int)
        for i, x in enumerate(nums):
            if target-x in seen:
                return [i, seen[target-x]]
            else:
                seen[x] = i
        return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        167. Two Sum II - Input Array Is Sorted
        """
        left, right = 0, len(nums)-1
        while left < right:
            sums = nums[left] + nums[right]
            if sums == target:
                return [left+1, right+1]
            if sums < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]


class TwoSum:
    """
    170. Two Sum III - Data structure design
    """

    def __init__(self):
        self.seen = defaultdict(int)

    def add(self, num: int) -> None:
        self.seen[num] += 1

    def find(self, value: int) -> bool:
        for x in self.seen:
            if value - x in self.seen:
                if value - x != x or self.seen[x] >= 2:
                    return True
        return False


class Solution:
    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:
        """
        653. Two Sum IV - Input is a BST
        BFS traverse the tree. Use a set to keep track of seen nodes.
        """
        seen = set()
        queue = [root]
        while queue:
            node = queue.pop(0)
            if target - node.val in seen:
                return True
            seen.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        993. Cousins in Binary Tree
        Preorder DFS iteration and record depth and parent of each node
        queue: (node, depth, parent)
        seen[node] = (depth, parent)
        cousin: same depth, different parents
        """
        if not root:
            return False

        seen = defaultdict(tuple)
        queue = [(root, 0, None)]
        while queue:
            node, depth, parent = queue.pop(0)
            if not node:
                continue
            if node.val in (x, y):
                seen[node.val] = (depth, parent)
            queue.append((node.left, depth+1, node))
            queue.append((node.right, depth+1, node))

        depthx, parentx = seen[x]
        depthy, parenty = seen[y]

        return depthx == depthy and parentx != parenty


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        """
        1214. Two Sum - Inputs are two BSTs
        Inorder traverse the two binary search trees and collect their values in two
        arrays (sorted in ascending order). Search for target with 2-pointer approach.
        Time: O(M+N), Space: O(M+N)
        """
        @lru_cache(None)
        def inorder(root: Optional[TreeNode]) -> List[int]:
            """
            Return array of inorder traversal of binary tree.
            Inorder: left -> root -> right. 
            """
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        nums1, nums2 = inorder(root1), inorder(root2)

        M, N = len(nums1), len(nums2)
        low, high = 0, N-1
        while low < M and high >= 0:
            if nums1[low] + nums2[high] == target:
                return True
            elif nums1[low] + nums2[high] < target:
                low += 1
            else:
                high -= 1

        return False


class Solution:
    def twoSumLessThanK(self, nums: List[int], target: int) -> int:
        """
        1099. Two Sum Less Than K
        Return max sum such that nums[i] + nums[j] = sum and sum < target
        """
        nums.sort()
        left, right = 0, len(nums)-1
        res = -1
        while left < right:
            x = nums[left] + nums[right]
            if x < target:
                left += 1
                res = max(res, x)
            else:
                right -= 1
        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        15. 3Sum (no dups in results)
        Sort nums -> 2sum
        """

        if len(nums) < 3:
            return []

        nums.sort()

        N = len(nums)
        res = []
        for i in range(N):
            if i >= 1 and nums[i] == nums[i-1]:
                continue

            target = -1 * nums[i]
            left, right = i+1, N-1

            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        return res


class Solution(object):
    def fourSum(self, nums, target):
        """
        4Sum: sort nums. [a,b,c,d] are distinct
        """
        N = len(nums)
        nums.sort()
        res = []
        for i in range(N):
            for j in range(i+1, N):
                left, right = j+1, N-1

                while left < right:
                    sums = nums[i] + nums[j] + nums[left] + nums[right]
                    if sums == target:
                        quad = [nums[i], nums[j], nums[left], nums[right]]
                        if quad not in res:
                            res.append(quad)
                        left += 1
                        right -= 1
                    elif sums < target:
                        left += 1
                    else:
                        right -= 1
        return res


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        454. 4Sum II. 
        Return the number of tuples from 4 lists summing to 0.
        """
        dic = collections.defaultdict(int)
        res = 0
        for x in nums1:
            for y in nums2:
                dic[x+y] += 1

        for p in nums3:
            for q in nums4:
                res += dic[-(p+q)]

        return res


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        938. Range Sum of BST
        Return the sum of all nodes within inclusive range [low, high].
        """
        if not root:
            return 0
        res = 0
        if root.val > low:
            res += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            res += self.rangeSumBST(root.right, low, high)
        if low <= root.val <= high:
            res += root.val
        return res


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        129. Sum Root to Leaf Numbers
        BFS for level order traverse
        Record (node, pre) when traversing the tree
        res += pre when reaching leaf node
        """
        queue = [(root, 0)]
        res = 0
        while queue:
            node, pre = queue.pop(0)
            pre = 10 * pre + node.val
            if not node.left and not node.right:
                res += pre
            if node.left:
                queue.append((node.left, pre))
            if node.right:
                queue.append((node.right, pre))
        return res


class Solution:
    @lru_cache(None)
    def sumNumbers(self, root: TreeNode, pre=0) -> int:
        """
        129. Sum Root to Leaf Numbers
        root = [1,2,3], res: 25 (12+13)
        """
        if not root:
            return 0
        pre = 10 * pre + root.val
        if not root.left and not root.right:
            return pre
        left = self.sumNumbers(root.left, pre)
        right = self.sumNumbers(root.right, pre)
        return left + right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        124. Binary Tree Maximum Path Sum.
        Return the max path sum of any non-empty path.
        Traverse the tree and retrieve each node's max path sum of left and right node.
        Compute the max path sum pass the current node and store it in res.
        Time: O(N), Space: O(N)
        """
        @lru_cache(None)
        def traverse(node):
            """Returns max path starting at node"""
            if not node:
                return 0
            left = max(traverse(node.left), 0)
            right = max(traverse(node.right), 0)
            res.append(left + node.val + right)
            return max(left, right) + node.val

        res = []
        traverse(root)
        return max(res)


class Solution:
    @lru_cache(None)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """404. Sum of all Left Leaves of binary tree"""
        def isLeaf(node):
            return node and not node.left and not node.right

        if not root:
            return 0
        if isLeaf(root.left):
            return root.left.val + self.sumOfLeftLeaves(root.right)

        left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)
        return left + right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """404. Sum of all Left Leaves of binary tree"""
        def isLeaf(node):
            return node and not node.left and not node.right

        res = 0
        queue = [(root, False)]
        while queue:
            node, isLeft = queue.pop(0)
            if isLeft and isLeaf(node):
                res += node.val
            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))
        return res


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """
        1302. Deepest Leaves Sum of binary tree
        """
        res = 0
        queue = [root]
        while queue:
            sumval = 0
            level = []
            for node in queue:
                if not node:
                    continue
                sumval += node.val
                level.append(node.left)
                level.append(node.right)
            if sumval:
                res = sumval
            queue = level
        return res


class Solution:
    def minSubArrayLen(self, nums: List[int], target: int) -> int:
        """ 
        209. Minimum Size Subarray Sum 
        nums = [2,3,1,2,4,3], target = 7, res: 2 (3 and 4)
        """
        left, res = 0, len(nums) + 1
        for right in range(len(nums)):
            target -= nums[right]
            while target <= 0:
                res = min(res, right - left + 1)
                target += nums[left]
                left += 1
        return res % (len(nums) + 1)


class Solution():
    def checkSubarraySum(self, nums: List[int], k: int) -> int:
        """
        523. Continuous Subarray Sum
        Return true if nums has a continuous subarray of size >= 2  
        summming up to a multiple of k, or false otherwise.
        Iterate through list and update dic: {csum: i}
        """
        seen = {0: -1}
        csum = 0
        for i, x in enumerate(nums):
            csum += x
            if k != 0:
                csum %= k
            if csum not in seen:
                seen[csum] = i
            elif i - seen[csum] >= 2:
                return True
        return False


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """
        325. Maximum Size Subarray Sum Equals k
        """
        seen = {0: -1}
        res = csum = 0
        for i, x in enumerate(nums):
            csum += x
            if csum-k in seen:
                res = max(res, i - seen[csum-k])
            seen.setdefault(csum, i)
        return res


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        1480. Running Sum of 1d Array
        [1,2,3,4] -> [1,3,6,10]
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums


class Solution:
    def sumOddLengthSubarrays(self, nums: List[int]) -> int:
        """
        1588. Sum of All Odd Length Subarrays
        Return the sum of all odd-length subarrays of nums
        """
        N = len(nums)
        res = 0
        for k in range(1, N + 1, 2):
            for i in range(N - k + 1):
                res += sum(nums[i:i+k])
        return res


class NumArray:
    """
    303. Range Sum Query - Immutable
    """

    def __init__(self, nums: List[int]):
        self.cumsum = nums
        for i in range(1, len(nums)):
            self.cumsum[i] += self.cumsum[i-1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.cumsum[right]
        return self.cumsum[right] - self.cumsum[left-1]


class NumArray:
    """
    307. Range Sum Query - Mutable
    Brute force, TLE
    """

    def __init__(self, nums: List[int]):
        self.diff = {}
        self.nums = nums
        self.csum = [0]
        for x in nums:
            self.csum.append(self.csum[-1] + x)

    def update(self, i: int, val: int) -> None:
        self.diff[i] = val - self.nums[i]

    def sumRange(self, i: int, j: int) -> int:
        res = self.csum[j+1] - self.csum[i]
        for key, val in self.diff.items():
            if i <= key <= j:
                res += val
        return res


class NumMatrix:
    """
    304. Range Sum Query 2D - Immutable
    """

    def __init__(self, matrix: List[List[int]]):
        M, N = len(matrix), len(matrix[0])
        self.csum = [[0]*(N+1) for _ in range(M+1)]
        for i, j in product(range(M), range(N)):
            self.csum[i+1][j+1] = matrix[i][j] + self.csum[i][j+1] \
                + self.csum[i+1][j] - self.csum[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x22 = self.csum[row2+1][col2+1]
        x11 = self.csum[row1][col1]
        x12 = self.csum[row1][col2+1]
        x21 = self.csum[row2+1][col1]
        return x22 - x12 - x21 + x11


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        1572. Matrix Diagonal Sum
        """
        N = len(mat)
        mid = N // 2
        res = 0
        for i in range(N):
            res += mat[i][i]
            res += mat[N-1-i][i]
        if N % 2:
            res -= mat[mid][mid]
        return res


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        1314. Matrix Block Sum
        """
        M, N = len(mat), len(mat[0])
        csum = [[0]*(N+1) for _ in range(M+1)]

        for i, j in product(range(M), range(N)):
            csum[i+1][j+1] = csum[i][j+1] + \
                csum[i+1][j] + mat[i][j] - csum[i][j]

        res = [[0]*N for _ in range(M)]
        for i, j in product(range(M), range(N)):
            r0, r1 = max(0, i-k), min(M-1, i+k)
            c0, c1 = max(0, j-k), min(N-1, j+k)
            res[i][j] = csum[r1+1][c1+1] - csum[r0][c1+1] - \
                csum[r1+1][c0] + csum[r0][c0]
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        39. Combination Sum. 
        candidates = [2,3,6,7], target = 7. res: [[2,2,3],[7]]
        Time: O(K^N), Space: O(K^N)
        where K = target/min(candidates) and N = len(candidates)
        """
        def backtrack(i, x):
            """Populate res via backtracking."""
            if x < 0:
                return
            if x == 0:
                res.append(stack.copy())
            for j in range(i, len(candidates)):
                stack.append(candidates[j])
                backtrack(j, x-candidates[j])
                stack.pop()
            return

        res, stack = [], []
        backtrack(i=0, x=target)
        return res


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        494. Target Sum. DP
        Two variables: index + sum
        Use a map of (sum : ways) to keep track
        Update map for each index interation
        """
        lookup = defaultdict(int)
        lookup[nums[0]] = lookup[-nums[0]] = 1

        for i in range(1, len(nums)):
            nextLookup = defaultdict(int)
            for sm in lookup:
                nextLookup[sm + nums[i]] += lookup[sm]
                nextLookup[sm - nums[i]] += lookup[sm]
            lookup = nextLookup

        return lookup[target]
