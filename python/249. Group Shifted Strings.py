"""
249. Group Shifted Strings
Medium

We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

Example 1:
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:
Input: strings = ["a"]
Output: [["a"]]
 
"""


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        Time: O(N * K), Space: O(N * K)
        """
        def hashkey(string: str):
            """
            Generate the Hash value, O(K) time/space
            """
            key = []
            for c1, c2 in zip(string[:-1], string[1:]):
                mod = (ord(c2) - ord(c1)) % 26 + ord('a')
                key.append(chr(mod))
            return ''.join(key)

        groups = collections.defaultdict(list)
        for s in strings:
            key = hashkey(s)
            groups[key].append(s)

        return list(groups.values())
