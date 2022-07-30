"""
455. Assign Cookies
Easy

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
"""


"""
Solution:
1) Starting from the child with less greediness
2) Assign the cookies to children if (g[i] <= s[i])
3) Maximize the number of happy children.
"""


class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for j in range(len(s)):
            if i < len(g) and g[i] <= s[j]:
                i += 1
        return i


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if g == [] or s == []:
            return 0

        g.sort()
        s.sort()
        res = 0
        for i in range(len(s)):
            if res < len(g) and s[i] >= g[res]:
                res += 1

        return res
