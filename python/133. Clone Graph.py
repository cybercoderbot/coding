"""
133. Clone Graph
Medium


Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


"""
Recursively(deep) copy the nodes being traversed. A caveat is that the node needs to be put in seen before adding neighbors. Otherwise, endless recursive calls will be induced.

"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # original -> clone mapping
        memo = {node: Node(node.val)}
        stack = [node]
        while stack:
            n = stack.pop()
            for nn in n.neighbors:
                if nn not in memo:
                    memo[nn] = Node(nn.val)
                    stack.append(nn)
                memo[n].neighbors.append(memo[nn])

        return memo[node]


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        queue = deque([node])
        clones = {node.val: Node(node.val, [])}
        while queue:
            p = queue.popleft()
            q = clones[p.val]

            for nbr in p.neighbors:
                if nbr.val not in clones:
                    clones[nbr.val] = Node(nbr.val, [])
                    queue.append(nbr)

                q.neighbors.append(clones[nbr.val])

        return clones[node.val]


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        def clone(node, memo):
            """Return deep-cloned graph."""
            if node not in memo:
                cloned = memo[node] = Node(node.val)
                cloned.neighbors = [clone(nn, memo) for nn in node.neighbors]

            return memo[node]

        return clone(node, memo={})
