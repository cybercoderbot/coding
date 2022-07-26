"""
246. Strobogrammatic Number
Easy

Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:
Input: num = "69"
Output: true


Example 2:
Input: num = "88"
Output: true

Example 3:
Input: num = "962"
Output: false
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        hmap = {"0": "0", "1": "1", "8": "8", "9": "6", "6": "9"}

        N = len(num)
        if N % 2 and num[N//2] not in "018":
            return False

        i,  j = 0, N-1
        while i < j:
            if num[i] not in hmap.keys() or num[j] not in hmap.keys():
                return False
            if hmap[num[i]] != num[j]:
                return False
            i += 1
            j -= 1

        return True


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        hmap = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        return all(hmap.get(num[i]) == num[~i] for i in range(len(num)//2+1))
