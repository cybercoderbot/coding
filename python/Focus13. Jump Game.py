class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        55. Jump Game. 
        Start at first index. Return true if you can reach the last index.
        """
        N = len(nums)
        i, maxPos = 0, 0

        while i <= maxPos:
            maxPos = max(maxPos, i + nums[i])
            if maxPos >= N - 1:
                return True
            i += 1

        return False


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        45. Jump Game II. 
        Start from first position, return the min number of jumps to reach the last position.
        """

        N = len(nums)
        if N <= 1:
            return 0
        left, right = 0, nums[0]
        res = 1
        while right < N - 1:
            res += 1
            nxt = max(i + nums[i] for i in range(left, right + 1))
            left, right = right, nxt

        return res


class Solution:
    def canReach(self, nums: List[int], start: int) -> bool:
        """
        1306. Jump Game III
        When you are at index i, you can jump to i + nums[i] or i - nums[i], check if you can reach to any index with value 0. You can not jump outside of the array at any time.
        """

        N = len(nums)
        queue = [start]

        while queue:
            node = queue.pop(0)

            if nums[node] == 0:
                return True

            for i in (node + nums[node], node - nums[node]):
                if 0 <= i < N:
                    queue.append(i)

            # mark as visited
            nums[node] = -nums[node]

        return False


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        """
        1345. Jump Game IV
        In one step you can jump from index i to index:

        1) i + 1 where: i + 1 < nums.length.
        2) i - 1 where: i - 1 >= 0.
        3) j where: nums[i] == nums[j] and i != j.

        Construct graph and BFS traverse the graph to find the end of array.
        """

        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)

        queue, seen = [0], {0}
        res = 0
        while queue:
            for _ in range(len(queue)):
                i = queue.pop(0)
                if i == len(nums)-1:
                    return res
                for j in [i-1, i+1] + pos[nums[i]]:
                    if 0 <= j < len(nums) and j not in seen:
                        seen.add(j)
                        queue.append(j)
                pos.pop(nums[i])
            res += 1

        return inf


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """
        1871. Jump Game VII

        You can move from index i to index j if:
        1) i + minJump <= j <= min(i + maxJump, s.length - 1), and 
        2) s[j] == '0'.

        BFS
        """

        queue, left = [0], 0
        for i in queue:
            if i == len(s)-1:
                return True
            low = max(left + 1, i + minJump)
            high = min(i + maxJump + 1, len(s))

            for j in range(low, high):
                if s[j] == "0":
                    queue.append(j)
            left = max(left, i + maxJump)

        return False


class Solution:
    def oddEvenJumps(self, nums: List[int]) -> int:
        """
        975. Odd Even Jump
        Jump to smallest indexes at odd-numbered jumps.
        Jump to largeest indexes at even-numbered jumps.
        Return the number of good starting indices (reach end)
        """
        N = len(nums)

        stack = []
        small = [-1] * N
        for i, x in sorted(enumerate(nums), key=lambda x: -x[1]):
            while stack and stack[-1] < i:
                small[stack.pop()] = i
            stack.append(i)

        stack = []
        large = [-1] * N
        for i, x in sorted(enumerate(nums), key=lambda x: x[1]):
            while stack and stack[-1] < i:
                large[stack.pop()] = i
            stack.append(i)

        odd = [0] * N
        even = [0] * N
        odd[-1] = even[-1] = 1
        for i in range(N-1, -1, -1):
            if 0 <= large[i]:
                odd[i] = even[large[i]]
            if 0 <= small[i]:
                even[i] = odd[small[i]]

        return sum(odd)
