"""
1980. Find Unique Binary String
Medium

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.


The trick to do this question is somewhat similar to Cantor's Diagonalization. You can read about it in detail here.

Since we are given that number of bits in the number is equal to number of elements.
What we can do is we create a binary string which differs from first binary at 1st position, second binary at 2nd position, third binary at 3rd position,...and so on.

This will make sure that the binary we have made is unique (as it differs from all others at atleast one position).

We create an empty string first.
And simply iterate through the binary strings while putting the flipped bit of ith bit of "binary at ith position".

	for(int i=0; i<nums.size(); i++) 
		ans+= nums[i][i]=='0' ? '1' : '0';
I have created this image explaining the process for test case ["111", "001", "010"] :
"""


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i, s in enumerate(nums):
            if s[i] == "1":
                res.append("0")
            else:
                res.append("1")

        return "".join(res)


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i, s in enumerate(nums):
            res.append(str(1-int(s[i])))

        return "".join(res)
