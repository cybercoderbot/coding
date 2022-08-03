"""
1245. Tree Diameter
Medium

The diameter of a tree is the number of edges in the longest path in that tree.
There is an undirected tree of n nodes labeled from 0 to n - 1. You are given a 2D array edges where edges.length == n - 1 and edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the tree.
Return the diameter of the tree.

Example 1:
Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: The longest path of the tree is the path 1 - 0 - 2.
"""


"""
starting from any node, apply (the 1st pass) BFS and retain the last node while traversing the tree
starting from the last node in the previous step, apply (the 2nd pass) BFS and return the max depth while traversing the tree.
"""


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # build tree
        connected = defaultdict(set)
        for x, y in edges:
            connected[x].add(y)
            connected[y].add(x)

        def bfs(node, level=0):
            """
            Graph BFS starting at given node by level. 
            Return last node in search and levels.
            """
            queue = [node]
            seen = set(queue)
            while queue:
                qnext = []
                for x in queue:
                    for y in connected[x]:
                        if y not in seen:
                            qnext.append(y)
                            seen.add(y)
                queue = temp
                level += 1
            return x, level - 1

        # two passes
        # 1st pass - find a node on longest path
        # 2nd pass - find length of longest path (i.e. diameter of the tree)
        node = bfs(0)[0]
        return bfs(node)[1]
