"""
In a tree nodes are uni-directional (parent=>child), 
In a graph neighbors are bi-directional (A<->B). 
When cloning graphs a dictionary is used to keep track of cloned nodes to avoid infinite loops
"""


class Solution:
    @lru_cache(None)
    def cloneGraph(self, node: 'Optional[Node]', memo={}) -> 'Optional[Node]':
        """
        133. Clone Graph. Recursive solution
        O(N) time, O(N) space
        """
        if not node:
            return None
        if node in memo:
            return memo[node]

        memo[node] = Node(node.val)
        for nn in node.neighbors:
            if nn not in memo:
                memo[nn] = self.cloneGraph(nn, memo)
        return memo[node]


class Solution:
    @lru_cache(None)
    def copyRandomList(self, head: 'Optional[Node]', memo={}) -> 'Optional[Node]':
        """
        138. Copy List with Random Pointer
        Return a deep copy of node.
        O(N) time, O(N) space
        """
        if not head:
            return None
        if head in memo:
            return memo[head]

        memo[head] = node = Node(head.val)
        node.next = self.copyRandomList(head.next, memo)
        node.random = self.copyRandomList(head.random, memo)
        return memo[head]


class Solution:
    @lru_cache(None)
    def copyRandomBinaryTree(self, root: 'Optional[Node]', memo={}) -> 'Optional[NodeCopy]':
        """
        1485. Clone Binary Tree With Random Pointer
        memo: track visited nodes to avoid cycles (endless copy)
        """
        if not root:
            return None
        if root in memo:
            return memo[root]

        node = NodeCopy(root.val)
        memo[root] = node
        node.left = self.copyRandomBinaryTree(root.left)
        node.right = self.copyRandomBinaryTree(root.right)
        node.random = self.copyRandomBinaryTree(root.random)
        return node


class Solution:
    @lru_cache(None)
    def cloneTree(self, root: 'Optional[Node]', memo={}) -> 'Optional[Node]':
        """
        1490. Clone N-ary Tree. Recursive solution
        O(N) time, O(N) space
        """
        if not root:
            return None

        node = Node(root.val)
        for child in root.children:
            node.children.append(self.cloneTree(child))
        return node


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        """
        1490. Clone N-ary Tree. Recursive solution
        O(N) time, O(N) space
        """
        if root is None:
            return None
        children = [self.cloneTree(child) for child in root.children]
        return Node(root.val, children)


class Solution:
    def cloneGraph(self, node: 'Optional[Node]') -> 'Optional[Node]':
        """
        133. Clone Graph
        Recursively deep copy the nodes being traversed.
        A node needs to be put in seen before adding neighbors.
        Otherwise, endless recursive calls will be induced.
        1) BFS to traverse the graph
        2) A hash map to keep track of visited and cloned nodes
        Time: O(V + E) - for BFS, Space: O(V) - for the hashmap
        """
        if not node:
            return None

        # original -> clone mapping
        clones = {node: Node(node.val)}
        queue = collections.deque([node])

        while queue:
            src = queue.popleft()
            for nn in src.neighbors:
                if nn not in clones:
                    clones[nn] = Node(nn.val)
                    queue.append(nn)
                clones[src].neighbors.append(clones[nn])

        return clones[node]


class Solution:
    def cloneGraph(self, node: 'Optional[Node]') -> 'Optional[Node]':
        """
        133. Clone Graph
        DFS Iteration using stack
        """
        if not node:
            return None

        memo = {node: Node(node.val)}
        stack = [node]
        while stack:
            node = stack.pop()
            for nn in node.neighbors:
                if nn not in memo:
                    memo[nn] = Node(nn.val)
                    stack.append(nn)
                memo[node].neighbors.append(memo[nn])
        return memo[node]


class Solution:
    @lru_cache(None)
    def copyRandomList(self, head: 'Optional[Node]', memo={}) -> 'Optional[Node]':
        """
        138. Copy List with Random Pointer
        Return a deep copy of node.
        O(N) time, O(N) space
        """
        if not head:
            return None
        if head in memo:
            return memo[head]

        memo[head] = node = Node(head.val)
        node.next = self.copyRandomList(head.next, memo)
        node.random = self.copyRandomList(head.random, memo)
        return memo[head]


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        138. Copy List with Random Pointer
        Return a deep copy of node.
        O(N) time, O(N) space
        """
        @lru_cache(None)
        def deepcopy(node):
            """Return a deep copy of node."""
            if not node:
                return None
            if node not in memo:
                copied = memo[node] = Node(node.val)
                copied.next = deepcopy(node.next)
                copied.random = deepcopy(node.random)
            return memo[node]

        memo = {}
        return deepcopy(node=head)


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        138. Copy List with Random Pointer
        2-pass iterative implementation
        O(N) time, O(N) space
        """
        if not head:
            return None

        memo = {}
        node, copied = head, Node(head.val)
        while node:
            memo[node] = copied = Node(node.val)
            node = node.next

        node = head
        while node:
            memo[node].next = memo.get(node.next)
            memo[node].random = memo.get(node.random)
            node = node.next
        return memo[head]


class Solution:
    @lru_cache(None)
    def copyRandomBinaryTree(self, root: 'Optional[Node]', memo={}) -> 'Optional[NodeCopy]':
        """
        1485. Clone Binary Tree With Random Pointer
        memo: track visited nodes to avoid cycles (endless copy)
        """
        if not root:
            return None
        if root in memo:
            return memo[root]

        node = NodeCopy(root.val)
        memo[root] = node
        node.left = self.copyRandomBinaryTree(root.left)
        node.right = self.copyRandomBinaryTree(root.right)
        node.random = self.copyRandomBinaryTree(root.random)
        return node


class Solution:
    @lru_cache(None)
    def copyRandomBinaryTree(self, root: 'Optional[Node]', memo={}) -> 'Optional[NodeCopy]':
        """
        1485. Clone Binary Tree With Random Pointer
        memo: track visited nodes to avoid cycles (endless copy)
        """
        if not root:
            return None
        if root in memo:
            return memo[root]

        node = NodeCopy(root.val)
        memo[root] = node
        memo[root].left = self.copyRandomBinaryTree(root.left)
        memo[root].right = self.copyRandomBinaryTree(root.right)
        memo[root].random = self.copyRandomBinaryTree(root.random)
        return memo[root]
