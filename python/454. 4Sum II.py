"""
454. 4Sum II
Medium

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1


Approach 1: Hashmap

1.
- For each a in A.
- For each b in B.
    If a + b exists in the hashmap m, increment the value.
    Else add a new key a + b with the value 1.
    For each c in C.

2.
- For each d in D.
- Lookup key -(c + d) in the hashmap m.
  Add its value to the count cnt.

3. Return the count cnt.


Complexity Analysis

Time Complexity: O(n^2). 
We have 2 nested loops to count sums, and another 2 nested loops to find complements.

Space Complexity: O(n^2). for the hashmap. There could be up to O(n^2) distinct a + b keys.


"""



class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        count = 0
        m = collections.defaultdict(int)
        for x in nums1:
            for y in nums2:
                m[x + y] += 1
                
        for z in nums3:
            for w in nums4:
                count += m[-(z + w)]
                
        return count