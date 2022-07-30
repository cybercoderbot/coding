"""
288. Unique Word Abbreviation
Medium

The abbreviation of a word is a concatenation of its first letter, the number of characters between the first and last letter, and its last letter. If a word has only two characters, then it is an abbreviation of itself.

For example:
dog --> d1g because there is one letter between the first letter 'd' and the last letter 'g'.
internationalization --> i18n because there are 18 letters between the first letter 'i' and the last letter 'n'.
it --> it because any word with only two characters is an abbreviation of itself.
Implement the ValidWordAbbr class:

ValidWordAbbr(String[] dictionary) Initializes the object with a dictionary of words.
boolean isUnique(string word) Returns true if either of the following conditions are met (otherwise returns false):
There is no word in dictionary whose abbreviation is equal to word's abbreviation.
For any word in dictionary whose abbreviation is equal to word's abbreviation, that word and word are the same.
 
Example 1:
Input
["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique", "isUnique"]
[[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"], ["cake"]]
Output
[null, false, true, false, true, true]
"""


class ValidWordAbbr:
    """
    Create a hash table to map key to words. Here a trick is that one doesn't have to follow the definition given by the problem. Instead, one could safely use ones own hashing algo. Here I use word[0] + str(len(word)) + word[-1] as the key.
    """

    def __init__(self, dictionary: List[str]):
        self.d = defaultdict(set)
        for word in set(dictionary):
            key = word[0] + str(len(word)) + word[-1]
            self.d[key].add(word)

    def isUnique(self, word: str) -> bool:
        key = word[0] + str(len(word)) + word[-1]
        return self.d[key] <= {word}
