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
Recursively (deep) copy the nodes being traversed. 
A caveat is that the node needs to be put in seen before adding neighbors. 
Otherwise, endless recursive calls will be induced.

"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # original -> clone mapping
        memo = {node: Node(node.val)}
        queue = [node]

        while queue:
            src = queue.pop(0)
            for nn in src.neighbors:
                if nn not in memo:
                    memo[nn] = Node(nn.val)
                    queue.append(nn)
                memo[src].neighbors.append(memo[nn])

        return memo[node]


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        queue = [node]
        memo = {node.val: Node(node.val, [])}
        while queue:
            src = queue.pop(0)
            dst = memo[src.val]

            for nn in src.neighbors:
                if nn.val not in memo:
                    memo[nn.val] = Node(nn.val, [])
                    queue.append(nn)

                dst.neighbors.append(memo[nn.val])

        return memo[node.val]


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        def clone(node, memo):
            """Return deep-cloned graph."""
            if node not in memo:
                cloned = Node(node.val)
                memo[node] = cloned
                cloned.neighbors = [clone(nn, memo) for nn in node.neighbors]

            return memo[node]

        return clone(node, memo={})
