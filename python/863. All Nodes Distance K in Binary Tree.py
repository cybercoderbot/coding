"""
863. All Nodes Distance K in Binary Tree
Medium

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
You can return the answer in any order.
"""


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        863. All Nodes Distance K in Binary Tree
        """
        # build graph as adjacency list
        graph = defaultdict(list)
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            for child in (node.left, node.right):
                if child:
                    queue.append(child)
                    graph[node.val].append(child.val)
                    graph[child.val].append(node.val)

        # bfs from target
        seen = set()
        queue = [target.val]
        while queue:
            if k == 0:
                break
            nextq = []
            for node in queue:
                seen.add(node)
                neighbors = [nn for nn in graph[node] if nn not in seen]
                nextq.extend(neighbors)
            k -= 1
            queue = nextq
        return queue
