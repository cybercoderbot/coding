"""
Sliding Window Problems

How do we recognize a sliding window problem? Well, there are three things to look for:

1. A question asking you to analyze a contiguous set of data (subarray, substring, etc)
2. A predefined condition that can be analyzed for each set of data
3. The max, min, longest, shortest, number of, etc things that meet the condition.

You can use the same sliding window algorithms with a couple different variations for almost every sliding window problem. This particular problem requires the use of a dynamically resizing sliding window (one that gets longer until it meets the condition and shrinks until it does not). I left comments for every piece of the code. It's a bit longer than the "concise" answers but I prefer a longer, more readable piece of code over a short and unreadable one. You could have also used an array to store the character frequencies but I like the hashmap implementation better in terms of readability.
"""


"""
239. Sliding Window Maximum
Hard

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        """
        Time: O(Nk), where N is number of elements in the array.
        Space: O(N−k+1) for an output array.
        TLE
        """
        N = len(nums)
        if N * k == 0:
            return []

        return [max(nums[i:i + k]) for i in range(N - k + 1)]


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        """
        Use a deque to keep indexes of the running maximum num

        Time: O(N)
        Space: O(N)
        """

        deq = []
        res = []
        for i, x in enumerate(nums):

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while deq and nums[deq[-1]] < x:
                deq.pop(-1)

            deq.append(i)

            # remove indexes of elements out of bound for sliding window
            while deq and i - deq[0] >= k:
                deq.pop(0)

            # if i + 1 < k, then we are initializing the bigger array
            if i + 1 >= k:
                res.append(nums[deq[0]])
        return res


"""
862. Shortest Subarray with Sum at Least K
Hard

Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.


Example 1:
Input: nums = [1], k = 1
Output: 1

Example 2:
Input: nums = [1,2], k = 4
Output: -1

Example 3:
Input: nums = [2,-1,2], k = 3
Output: 3
"""


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = inf
        deq = [(-1, 0)]
        presum = 0
        for i, x in enumerate(nums):
            presum += x
            while deq and presum - deq[0][1] >= k:
                start, _ = deq.pop(0)
                res = min(res, i - start)
            while deq and deq[-1][1] >= presum:
                deq.pop(-1)
            deq.append((i, presum))

        return res if res < inf else -1


"""
904. Fruit Into Baskets
Medium

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 
Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
"""


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        start = 0

        for i, v in enumerate(fruits):
            freq[v] += 1

            if len(freq) > 2:
                pre = fruits[start]
                freq[pre] -= 1
                if freq[pre] == 0:
                    freq.pop(pre)

                start += 1

        return i - start + 1
