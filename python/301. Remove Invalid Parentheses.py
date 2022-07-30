"""
301. Remove Invalid Parentheses
Hard

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

Example 1:
Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:
Input: s = ")("
Output: [""]
"""


from collections import deque


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        count = 0
        for c in string:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        res = []

        # BFS Solution
        visited = {s}
        queue = deque([(s, 0)])
        found, nmin = False, len(s)

        while queue:
            current, nchanges = queue.popleft()

            if found and nmin < nchanges:
                break

            # validate current
            if isValid(current):
                # add to res
                found = True
                nmin = nchanges
                res.append(current)
            else:
                for i in range(len(current)):
                    candidate = current[:i] + current[i+1:]

                    # we might create duplicate string -> s='())'
                    # when we remove i=1 or i=2 and result in the same s
                    if candidate not in visited:
                        queue.append((candidate, nchanges+1))
                        visited.add(candidate)

        return res
