"""
294. Flip Game II
Medium

You are playing a Flip Game with your friend.

You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return true if the starting player can guarantee a win, and false otherwise.

Example 1:
Input: currentState = "++++"
Output: true
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Example 2:
Input: currentState = "+"
Output: false
"""


class Solution:
    @lru_cache(None)
    def canWin(self, s: str) -> bool:
        for i in range(len(s)-1):
            if s[i:i+2] == '++' and not self.canWin(s[:i]+'--'+s[i+2:]):
                return True
        return False


class Solution:
    def canWin(self, s: str, memo={}) -> bool:

        if s in memo:
            return memo[s]

        for i in range(len(s)-1):
            if s[i:i+2] == '++' and not self.canWin(s[:i]+'--'+s[i+2:]):
                memo[s] = True
                return True
        memo[s] = False

        return False
