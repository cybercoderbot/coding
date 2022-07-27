"""
207. Course Schedule
Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""


class Solution:
    def canFinish(self, N: int, prereq: List[List[int]]) -> bool:
        """
        Topolotical sort via DFS
        """

        graph = defaultdict(list)  # digraph
        for pre, cur in prereq:
            graph[cur].append(pre)

        def cyclic(cur):
            """Return True if cycle is detected."""
            if visited[cur]:
                return visited[cur] == 1
            visited[cur] = 1
            for pre in graph[cur]:
                if cyclic(pre):
                    return True
            visited[cur] = 2
            return False

        visited = [0] * N
        for x in range(N):
            if cyclic(x):
                return False
        return True


class Solution:
    def canFinish(self, N: int, prereq: List[List[int]]) -> bool:
        """
        Topolotical sort via BFS
        """
        indeg = [0]*N
        graph = defaultdict(list)
        for pre, cur in prereq:
            indeg[pre] += 1
            graph[cur].append(pre)

        stack = [i for i, x in enumerate(indeg) if not x]
        res = []
        while stack:
            x = stack.pop()
            res.append(x)
            for xx in graph[x]:
                indeg[xx] -= 1
                if indeg[xx] == 0:
                    stack.append(xx)
        return len(res) == N
