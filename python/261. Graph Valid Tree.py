"""
261. Graph Valid Tree
Medium

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
"""


class Solution:
    def dfs(self, node, parent, graph, visited):
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                if self.dfs(nbr, node, graph, visited):
                    return True
            elif nbr in visited and nbr != parent:
                return True
        return False

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            u, v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)
        visited = set([])
        if self.dfs(0, -1, graph, visited):
            return False
        if len(visited) != n:
            return False
        return True


class Solution():
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Union Find: Quick Find
        If an edge end points are already part of same component, then we have cycle.
        Also, we must make sure number of edges is equal to n-1
        Quick Find implementation of Union Find is O(V * E)
        For every edge, we might have to update the entire component array which is size N
        """
        visited = [i for i in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            p, q = visited[u], visited[v]

            if p == q:
                return False
            else:
                for i, x in enumerate(visited):
                    if x == p:
                        visited[i] = q

        return len(edges) == n - 1
