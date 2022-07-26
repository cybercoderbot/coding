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
    """
    Complexity

    Let N be the length of strings and K be the maximum length of a string in strings.

    Time complexity: O(N*K)
    We iterate over all N strings and for each string, we iterate over all the characters to generate 
    the Hash value, which takes O(K) time. To sum up, the overall time complexity is O(N*K).

    Space complexity: O(N*K)
    We need to store all the strings plus their Hash values in mapHashToList. In the worst scenario, 
    when each string in the given list belongs to a different Hash value, the maximum number of strings 
    stored in mapHashToList is 2*N. Each string takes at most O(K) space. Hence the overall space 
    complexity is O(N*K).

    """

    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def get_hashkey(string: str):
            key = []
            for c1, c2 in zip(string[:-1], string[1:]):
                mod = (ord(c2) - ord(c1)) % 26 + ord('a')
                key.append(chr(mod))
            return ''.join(key)

        groups = collections.defaultdict(list)

        for s in strings:
            key = get_hashkey(s)
            groups[key].append(s)

        return list(groups.values())


# Analysis
# Time complexity O(N)
# Space complexity O(N)
