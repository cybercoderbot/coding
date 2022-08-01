"""
1019. Next Greater Node In Linked List
Medium

You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

Example 1:
Input: head = [2,1,5]
Output: [5,5,0]

Example 2:
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
"""

# Similar to 503. Next Greater Element II, I am giving two solutions here.


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        """
        Solution 1 - forward approach
        Time: O(N), Space: O(N)
        """
        res, stack = [], []
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append((len(res), head.val))
            res.append(0)
            head = head.next
        return res


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        """
        Solution 2 - backward approach
        Time: O(N), Space: O(N)
        """
        prev, node = None, head
        while node:
            node.next, node, prev = prev, node.next, node

        node = prev
        res, stack = [], []
        while node:
            while stack and stack[-1] <= node.val:
                stack.pop()
            res.append(stack[-1] if stack else 0)
            stack.append(node.val)
            node = node.next
        return res[::-1]


"""
496. Next Greater Element I
Easy

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
"""


class Solution:

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Time: O(N), N = num of elements in nums2
        Space: O(N)
        """
        res = []
        stack = []
        m = {}

        for x in nums2:
            while stack and x > stack[-1]:
                m[stack[-1]] = x
                stack.pop()
            stack.append(x)

        # unmatched vals
        for x in stack:
            m[x] = -1

        for x in nums1:
            res.append(m[x])

        return res


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack, m = [], {}
        for x in nums2:
            while stack and stack[-1] < x:
                m[stack.pop()] = x
            stack.append(x)

        return [m.get(x, -1) for x in nums1]


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return None

        m = {}
        res = []
        stack = []
        stack.append(nums2[0])

        for i in range(1, len(nums2)):
            # if stack is not empty, then compare it's last element with nums2[i]
            while stack and nums2[i] > stack[-1]:
                # if the new element is greater than stack's top element, then add this to dictionary
                m[stack[-1]] = nums2[i]
                # since we found a pair for the top element, remove it.
                stack.pop()
            # add the element nums2[i] to the stack because we need to find a number greater than this
            stack.append(nums2[i])

        # for those in the stack for which we didn't find a greater number, map them to -1
        for x in stack:
            m[x] = -1

        for i in range(len(nums1)):
            res.append(m[nums1[i]])

        return res


"""
503. Next Greater Element II
Medium

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
"""


"""
Use the stack to record the reversed array nums. Loop the array from last integer to the first one. If the last integer in stack is bigger than the current interger in array, we have found the answer. Otherwise, we need to keep pop up the integer in stack. Besides, we need to push the current integer to the stack in each step.
"""


class Solution(object):
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = nums[::-1]
        res = []
        for x in reversed(nums):
            while stack and x >= stack[-1]:
                stack.pop()
            res.append(stack[-1] if stack else -1)
            stack.append(x)

        return res[::-1]


class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = nums[::-1]

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
        return res


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Approach 1 - backward
        """
        ans, stack = [], []
        # mono-stack (decreasing)
        for x in reversed(nums + nums):
            while stack and stack[-1] <= x:
                stack.pop()
            ans.append(stack[-1] if stack else -1)
            stack.append(x)
        ans.reverse()
        return ans[:len(nums)]


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Approach 2 - forward
        """
        ans = [-1]*len(nums)
        stack = []
        for i, x in enumerate(nums + nums):
            while stack and stack[-1][1] < x:
                ans[stack.pop()[0]] = x
            stack.append((i % len(nums), x))
        return ans


"""
556. Next Greater Element III
Medium

Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

Example 1:
Input: n = 12
Output: 21

Example 2:
Input: n = 21
Output: -1
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        Time complexity O(logN)
        Space complexity O(logN)
        """
        s = list(str(n))
        for i in reversed(range(len(s)-1)):
            if s[i] < s[i+1]:
                break
        else:
            return -1  # no break encounter

        for j in reversed(range(i+1, len(s))):
            if s[i] < s[j]:
                break
        s[i], s[j] = s[j], s[i]  # swap

        x, y = i+1, len(s)-1  # reverse
        while x < y:
            s[x], s[y] = s[y], s[x]
            x += 1
            y -= 1
        res = int("".join(s))
        return res if res < 2**31 else -1


"""
31. Next Permutation
Medium

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
"""


def nextPermutation(self, nums):
    """ Time O(N), Space O(1) in place"""

    idx1 = next((i for i in range(len(nums) - 2, -1, -1)
                 if nums[i] < nums[i + 1]), None)

    if idx1 is None:
        # [3,2,1] -> [1,2,3]:
        nums.sort()
    else:
        idx2 = next((i for i in range(len(nums) - 1, idx1, -1)
                     if nums[i] > nums[idx1]), None)
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
        nums[idx1 + 1:] = sorted(nums[idx1 + 1:])

    return


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Look for the last occurrence of an adjacent increasing pair nums[k-1] and nums[k];
        look for the smallest numbers (say at j) in nums[k:] that is larger than nums[k-1];
        swap nums[k-1] and nums[j];
        reverse numbers in nums[k:].
        Time: O(N), Space: O(1)
        """
        k = len(nums)-1
        while k and nums[k-1] >= nums[k]:
            k -= 1

        if k:
            lo, hi = k, len(nums)
            while lo < hi:
                mid = (lo + hi)//2
                if nums[mid] <= nums[k-1]:
                    hi = mid
                else:
                    lo = mid+1
            nums[k-1], nums[lo-1] = nums[lo-1], nums[k-1]

        lo, hi = k, len(nums)-1
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo, hi = lo+1, hi-1
