"""
277. Find the Celebrity
Medium

Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) that tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.
Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

Example 1:
Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:
Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.
"""


class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        At first, we assume person 0 is the celebrity. Then, we check if he/she knows 1.
        If so, 0 cannot be the celebrity as the celebrity doesn't know anyone. 
        Instead we assume person 1 is the celebrity.
        If not, 1 cannot be the celebrity as everyone knows the celebrity. 
        We keep assuming 0 is the celebrity.
        We keep the check until get a candidate. 
        Then, we confirm if indeed everyone knows him/her and he/she doesn't know anyone.
        """
        k = 0
        for i in range(1, n):
            if knows(k, i):
                k = i

        for i in range(n):
            if i == k:
                continue
            elif knows(k, i):
                return -1
            elif not knows(i, k):
                return -1
        return k


class Solution:
    def findCelebrity(self, n: int) -> int:
        k = 0
        for i in range(1, n):
            if knows(k, i):
                k = i

        x = all(knows(i, k) for i in range(n))
        y = not any(knows(k, i) for i in range(n) if i != k)
        return k if x and y else -1
