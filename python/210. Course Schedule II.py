"""
210. Course Schedule II
Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3]."""


class Solution:
    def findOrder(self, N: int, prereq: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for pre, cur in prereq:
            graph[cur].append(pre)

        def cyclic(x):
            """Return True if cycle is deteced."""
            if visited[x]:
                return visited[x] == 1

            visited[x] = 1
            for xx in graph.get(x, []):
                if cyclic(xx):
                    return True

            res.append(x)
            visited[x] = 2
            return False

        res = []
        visited = [0] * N
        for x in range(N):
            if cyclic(x):
                return []

        return res[::-1]


class Solution:
    def findOrder(self, N: int, prereq: List[List[int]]) -> List[int]:
        """
        Approach 2 - topoligical sort via Kahn's algo
        """
        graph = [[] for _ in range(N)]
        indeg = [0] * N

        for pre, cur in prereq:
            graph[cur].append(pre)
            indeg[pre] += 1

        res = []
        for i, pre in enumerate(indeg):
            if pre == 0:
                res.append(i)

        for cur in res:
            for pre in graph[cur]:
                indeg[pre] -= 1
                if indeg[pre] == 0:
                    res.append(pre)

        return res if len(res) == N else []
