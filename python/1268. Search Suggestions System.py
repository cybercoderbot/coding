"""
1268. Search Suggestions System
Medium


You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

 

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
"""


"""
Hash table
"""


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        mp = defaultdict(list)
        products = sorted(products)
        for prod in products:
            for i in range(len(prod)):
                mp[prod[:i+1]].append(prod)

        ans = []
        N = len(searchWord)
        for i in range(N):
            ans.append(mp[searchWord[:i+1]][:3])
        return ans


"""
# Approach 2 - 2 pointers
# Define two pointers lo and hi which mark the beginning and end of products matching prefixes in searchWord.
"""


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        N = len(products)
        low, high = 0, N-1
        for i, c in enumerate(searchWord):
            while low < N and (len(products[low]) <= i or products[low][i] < c):
                low += 1
            while high >= 0 and (len(products[high]) <= i or c < products[high][i]):
                high -= 1
            ans.append(products[low: min(low+3, high+1)])
        return ans
