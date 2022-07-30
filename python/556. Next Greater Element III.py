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


"""
Solution
Let us start from example and see how our algorithm should work.
Imagine n = 234157641. Our goal is to find next number with the same digits, which is greater than given one and which is the smallest one. It makes sense to try to take our number as close to original one as possible. Let us try to do it: can it start from 2......, yes, for example 24.... Can it start with 2341...? Yes, it can be 23417.... Can it start with 23415...? No, it can not, and the reason, that the rest what we have 7641 already biggest number given digits 7, 6, 4, 1.
So, we can see now, how our algorithm should work:

Start from the end and look for increasing pattern, it our case 7641.
If it happen, that all number has increasing pattern, there is no bigger number with the same digits, so we can return -1.
Now, we need to find the first digit in our ending, which is less or equal to digits[i-1]: we have ending 5 7641 and we are looking for the next number with the same digits. What can go instead of 5: it is 6! Let us change these two digits, so we have 6 7541 now. Finally, we need to reverse last ditits to get 6 1457 as our ending.
Complexity: time complexity is O(m), where m is number of digits in our number, space complexity O(m) as well.

PS see also problem 31. Next Permutation, which uses exactly the same idea.
"""


class Solution:
    def nextGreaterElement(self, n):
        """
        Time complexity O(N)
        Space complexity O(N)
        """
        nums = list(str(n))

        # 5 7641 -> 5
        i = len(nums) - 1
        while i-1 >= 0 and nums[i] <= nums[i-1]:
            i -= 1

        if i == 0:
            return -1

        # i = j = 1
        j = i
        while j+1 < len(nums) and nums[j+1] > nums[i-1]:
            j += 1
        # j = 2

        # 5 7641 -> 6 7541
        nums[i-1], nums[j] = nums[j], nums[i-1]

        # 6 7541 -> 6 1457
        nums[i:] = nums[i:][::-1]

        res = int(''.join(nums))

        return res if res < pow(2, 31) else -1


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
