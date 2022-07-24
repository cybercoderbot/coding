"""
1524. Number of Sub-arrays With Odd Sum
Medium

Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:
Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.


Example 2:
Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.


Example 3:
Input: arr = [1,2,3,4,5,6,7]
Output: 16
"""


"""
Idea
This is an elementary dynamic programming problem.
odd[i] records the number of subarray ending at arr[i] that has odd sum.
even[i] records the number of subarray ending at arr[i] that has even sum.
if arr[i + 1] is odd, odd[i + 1] = even[i] + 1 and even[i + 1] = odd[i]
if arr[i + 1] is even, odd[i + 1] = odd[i] and even[i + 1] = even[i] + 1
Since we only required the previous value in odd and even, we only need O(1) space.

Please upvote if you find this post helpful or interesting. It means a lot to me. Thx~

Complexity

Time: O(n)
Space: O(1)

"""


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = odd = even = 0
        mod = 10 ** 9 + 7
        for n in arr:
            even += 1
            if n % 2:
                odd, even = even, odd
            res = (res + odd) % mod
        return res


"""
odd number - even numer = odd number(e.g., 9 - 4=5)
even number - odd number = odd number(e.g., 8 - 3=5)
prefix sum: to obtain the sum of subarray arr[i + 1, j], we can use prefix sum by sum[0, j] - sum[0, i].
Idea:

Keep two counters, odd_sum and even_sum for the number of odd sums and even sums
Iterate through the array and during each iteration, keep the the sum of elements we've seen so far in curr_sum
Say the current index is j, if curr_sum is odd, we can decrease curr_sum by any previously seen even sum(say index i) to get a subarray arr[i + 1, j] with an odd sum
similarly, if curr_sum is even, we can decrease curr_sum by any previously seen odd sum to get a subarray with an odd sum.
even_sum initialize to be 1 since before we start and curr_sum = 0, 0 is even.

Time: O(n) - one pass
Space: O(1)
"""


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod, n = 10 ** 9 + 7, len(arr)
        odd, even, cumsum, res = 0, 1, 0, 0

        for i in arr:
            cumsum += i
            if cumsum % 2 == 1:
                odd += 1
                res += even % mod
            else:
                even += 1
                res += odd % mod

        return res % mod


"""
I know a lot of others also share this idea, but I was having a hard time solving this problem during the contest(got 1 TLE and 1 error before my solution got accepted), and that's why I wanna explain it in details.
If you find this post helpful, please upvote. Thank you.

This question gives us an array of integers arr, and asks how many sub-arrays there are that have an odd sum, modulo 10^9 + 7, since the values may grow large. Whenever we see a question with sub-arrays (or subsequences), the first thought is generally "How can we do this with some kind of DP?".

In this case, there are two key realizations: the first is that the only information we care about for a subarray is whether its sum is odd or even: if we "extend" a subarray by concatenating an adjacent element, we only need know whether the previous sum was odd or even and whether the next element is odd or even in order to determine whether the new subarray is odd or even.

The second is that we can reduce this further by just keeping track of how many odd and how many even sum subarrays there are that end at a given index. The idea to use "ending at a specific index" is to some extent gained through intuition by doing similar DP questions, but once we know that, it's fairly easy to see that at each index, the following holds:

If arr[idx] is even,

the number of odd sum subarrays ending at idx is equal to the number of odd sum subarrays ending at idx - 1
the number of even sum subarrays ending at idx is equal to the number of even sum subarrays ending at idx - 1 plus one, since we can start a new even sum subarray of length 1 at idx
Likewise, if arr[idx] is odd,

the number of odd sum subarrays ending at idx is equal to the number of even sum subarrays ending at idx - 1 plus one, since we can start a new odd sum subarray of length 1 at idx
the number of even sum subarrays ending at idx is equal to the number of odd sum subarrays ending at idx - 1
Putting this together,
"""


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = odd = even = 0
        mod = 10 ** 9 + 7
        for n in arr:
            if n % 2 == 0:
                even, odd = even + 1, odd
            else:
                even, odd = odd, even + 1
            res = (res + odd) % mod
        return res % mod
