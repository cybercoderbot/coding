"""
293. Flip Game
Easy

You are playing a Flip Game with your friend.

You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return all possible states of the string currentState after one valid move. You may return the answer in any order. If there is no valid move, return an empty list [].

Example 1:
Input: currentState = "++++"
Output: ["--++","+--+","++--"]

Example 2:
Input: currentState = "+"
Output: []
"""


class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        """
        Loop through s and look for ++
        If ++ is found, add the string with ++ replaced by -- to answer.
        """

        res = []
        for i in range(len(s)-1):
            if s[i:i+2] == "++":
                res.append(s[:i]+"--"+s[i+2:])
        return res


class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        """
        Loop through s and look for ++
        If ++ is found, add the string with ++ replace by -- to answer.
        """
        return [s[:i]+"--"+s[i+2:] for i in range(len(s)-1) if s[i:i+2] == "++"]
