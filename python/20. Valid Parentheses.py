"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s: 
            if c in pairs.keys(): 
                stack.append(c) 
            elif not stack:
                return False
            elif pairs[stack.pop()] != c: 
                return False 
            
        return len(stack) == 0
        