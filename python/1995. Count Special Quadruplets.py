"""
1995. Count Special Quadruplets
Easy

Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

nums[a] + nums[b] + nums[c] == nums[d], and a < b < c < d
 
Example 1:
Input: nums = [1,2,3,6]
Output: 1
Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.

Example 2:
Input: nums = [3,3,6,4,5]
Output: 0
Explanation: There are no such quadruplets in [3,3,6,4,5].

Example 3:
Input: nums = [1,1,1,3,5]
Output: 4
Explanation: The 4 quadruplets that satisfy the requirement are:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5

A little explanation:

The target is to find the number of quadruplet (a, b, c, d), which satisfies: nums[a] + nums[b] + nums[c] = nums[d],
We can transform it to: nums[a] + nums[b] = nums[d] - nums[c]

We can iterate a and b, get the sum of nums[a] and nums[b], and then see how many pairs of (c, d), such that
nums[a] + nums[b] = nums[d] - nums[c]

For example:
    nums = [1, 2, 3, 4, 9, 5, 10]
               a  b

    if we have a = 1, b = 2 (a, b are index)
    then nums[a] + nums[b] = 2 + 3 = 5
    then let's see how many pairs (c, d) such that nums[d] - nums[c] = 5

    Actually, here are two pairs (c = 3, d = 4) and (c = 5, d = 6), which meet the requirement.
    nums = [1, 2, 3, 4, 9, 5, 10]
               a  b  c  d

    nums = [1, 2, 3, 4, 9, 5, 10]
               a  b        c  d

So while we are at the index pair (a, b), we want to know the number of (c, d), which satisfy two conditions:
    • nums[a] + nums[b] = nums[d] - nums[c]
    • a < b < c < d                         
Actually, we can just enumerate all the (c, d) pairs after the index b, but it is too slow, which is O(n^2),
so the total will be O(n^4)

We can use map, the key is the difference: nums[d] - nums[c], the value is the number of pairs: (c, d)
While we iterate (a, b), we can also update this map.

We need to iterate (a, b) in the reverse order, because the difference map can be updated easily.
We still use nums = [1, 2, 3, 4, 9, 5, 10] as an example:
1st round:
    nums = [1, 2, 3, 4, 9, 5, 10]
                        b          
    map = {5: 1} because there is one pair (c = 5, d = 6), diff = nums[6] - nums[5] = 5
    
2nd round:
    nums = [1, 2, 3, 4, 9, 5, 10]
                     b
    map will be updated, there are two new pairs: (c = 4, d = 5), (c = 4, d = 6)   
    So map = {5: 1, 1: 1, -4: 1}

3rd round:
    nums = [1, 2, 3, 4, 9, 5, 10]
                  b
    map will be updated, there are three new pairs: (c = 3, d = 4), (c = 3, d = 5), (c = 3, d = 6)   
    So map = {5: 2, 1: 2, -4: 1, 6: 1}

You can see each time we update the map, we can directly use all the index x after the index b, and get
the difference: nums[x] - nums[b], and then use it to update the map.
"""


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count, N = 0, len(nums)
        m = defaultdict(int)

        for i in range(N):

            for j in range(i+1, N):
                count += m[nums[j] - nums[i]]

            for k in range(i):
                m[nums[k] + nums[i]] += 1

        return count


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res, N = 0, len(nums)
        count = defaultdict(int)  # type: int, default = 0

        # find a + b == d - c, and a < b < c < d
        for i in range(N - 1, 0, -1):
            # res += the numbers of cases which a + b == d - c.
            # a: nums[j], b: nums[i], c: previous nums[i]
            for j in range(i - 1, -1, -1):
                res += count[nums[i] + nums[j]]

            # count d - c, d: nums[j], c: nums[i], start from the end of nums, because a < b < c < d
            for j in range(l - 1, i, -1):
                count[nums[j] - nums[i]] += 1

        return res


class Solution:

    def countQuadruplets(self, nums: List[int]) -> int:
        count, N = 0, len(nums)
        m = defaultdict(int)

        for i in range(N-1, 0, -1):

            # res += the numbers of cases which a + b == d - c.
            # a: nums[j], b: nums[i], c: previous nums[i]
            for j in range(i-1, -1, -1):
                count += m[nums[i] + nums[j]]

            # count d - c,
            # d: nums[j], c: nums[i], start from the end of nums, because a < b < c < d
            for k in range(N-1, i, -1):
                m[nums[k] - nums[i]] += 1

        return count


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res = 0
        l = len(nums)

        count = defaultdict(lambda: 0)
        count[nums[l-1] - nums[l-2]] = 1

        for b in range(l - 3, 0, -1):
            for a in range(b - 1, -1, -1):
                res += count[nums[a] + nums[b]]

            for x in range(l - 1, b, -1):
                count[nums[x] - nums[b]] += 1

        return res
