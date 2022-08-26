class Solution:
    """
    Output city names based on population
    Straightforward, should be bug free
    Testing: corner cases on the indexes
    Time: O(N), or O(logN) using binary search
    """

    def __init__(self, cities: List[str], populations: List[int]):
        self.N = len(cities)
        self.cities = cities
        self.pdf = [p / sum(populations) for p in populations]
        self.cdf = self.pdf.copy()
        for i in range(1, self.N):
            self.cdf[i] += self.cdf[i-1]

    def selectCities(self) -> int:
        rand = random.random()
        for i, x in enumerate(self.cdf):
            if rand <= x:
                return self.cities[i]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        347. Top K Frequent Elements
        nums = [1,1,1,2,2,3], k = 2 -> [1,2]
        Bucket sort: map frequency to a list of numbers
        Time: O(N), Space O(N)
        """
        count = defaultdict(int)
        N = len(nums)
        for x in nums:
            count[x] += 1

        freq = [[] for i in range(N + 1)]
        for x, c in count.items():
            freq[c].append(x)

        res = []
        for i in range(N, -1, -1):
            res.extend(freq[i])
            if len(res) >= k:
                return res[:k]


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        692. Top K Frequent Words
        Return the answer sorted by the frequency from highest to lowest. 
        SORT the words with the same frequency by lexicographical order.
        """
        count = defaultdict(int)
        N = len(words)
        for w in words:
            count[w] += 1

        freq = [[] for i in range(N + 1)]
        for w, c in count.items():
            freq[c].append(w)

        res = []
        for i in range(N, -1, -1):
            res.extend(sorted(freq[i]))
            if len(res) >= k:
                return res[:k]


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        1762. Buildings With an Ocean View
        A building has an ocean view if all the rightside buildings are shorter.
        Return a list ofof buildings that have an ocean view.
        heights = [4,2,3,1] -> [0,2,3]
        Use a deque to store indexes.
        """
        N = len(heights)
        deq = collections.deque([N-1])
        for i in range(N - 2, -1, -1):
            if heights[i] > heights[deq[0]]:
                deq.appendleft(i)
        return deq


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        1762. Buildings With an Ocean View
        Use a decreasing mono-stack to store indices of heights
        """
        stack = []
        for i, x in enumerate(heights):
            while stack and heights[stack[-1]] <= x:
                stack.pop()
            stack.append(i)
        return stack


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        235. Lowest Common Ancestor of a BST
        """
        if not root:
            return None

        node = root
        while node:
            if all(x < node.val for x in [p.val, q.val]):
                node = node.left
            elif all(x > node.val for x in [p.val, q.val]):
                node = node.right
            else:
                return node


class Solution:
    @lru_cache(None)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        236. Lowest Common Ancestor of a Binary Tree
        (p and q are guaranteed to EXIST in the tree)
        All Node.val are unique. p != q
        """
        if not root or root in (p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        lca, self.deepest = None, 0

        def helper(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node:
                return depth
            left = helper(node.left, depth + 1)
            right = helper(node.right, depth + 1)
            if left == right == self.deepest:
                self.lca = node
            return max(left, right)

        helper(root, 0)
        return self.lca


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        """
        865. Smallest Subtree with all the Deepest Nodes
        1123. Lowest Common Ancestor of Deepest Leaves
        At each node, compute the depth of its left and right child.
        1) If left == right, deepest nodes in both the left and right subtree, 
           return node
        2) If left > right, deepest nodes only in the left subtree, move to node.left
        3) If left < right, deepest nodes only in the right subtree, move to node.left 
        Time O(N), Space O(N)
        """
        @lru_cache(None)
        def depth(node):
            """Return depth of tree rooted at node."""
            if not node:
                return 0
            left, right = depth(node.left), depth(node.right)
            return max(left, right) + 1

        node = root
        while node:
            left, right = depth(node.left), depth(node.right)
            if left > right:
                node = node.left
            elif left < right:
                node = node.right
            else:
                return node


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        """
        865. Smallest Subtree with all the Deepest Nodes
        1123. Lowest Common Ancestor of Deepest Leaves
        """
        if not root:
            return None

        parent = {}
        queue = collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node)
                if node.left:
                    queue.append(node.left)
                    parent[node.left] = node
                if node.right:
                    queue.append(node.right)
                    parent[node.right] = node

        while len(level) > 1:
            ancestors = set()
            for node in level:
                ancestors.add(parent[node])
            level = list(ancestors)
        return level[0]


class Solution:
    @lru_cache(None)
    def lowestCommonAncestor(self, root: TreeNode, nodes: List[TreeNode]) -> TreeNode:
        """
        1676. Lowest Common Ancestor of a Binary Tree IV
        All nodes exist in the tree. All node vals are unique.
        """
        nodes = set(nodes)
        if not root or root in nodes:
            return root

        left = self.lowestCommonAncestor(root.left, nodes)
        right = self.lowestCommonAncestor(root.right, nodes)
        if left and right:
            return root
        else:
            return left or right


class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        """
        1740. Find Distance in a Binary Tree
        Find the LCA, it is guaranteed to be on the path between p and q.
        Return the distance(LCA->p) + distance(LCA->q)
        Time: O(N), Space: O(logN)
        """
        def getLca(root: TreeNode, p: int, q: int) -> TreeNode:
            if not root:
                return None
            if root.val in (p, q):
                return root
            left = getLca(root.left, p, q)
            right = getLca(root.right, p, q)
            if left and right:
                return root
            return left or right

        @lru_cache(None)
        def dist(node, target):
            if not node:
                return inf
            if node.val == target:
                return 0
            left = dist(node.left, target)
            right = dist(node.right, target)
            return min(left, right) + 1

        lca = getLca(root, p, q)
        left = dist(lca, p)
        right = dist(lca, q)
        return left + right


class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        """
        Traverse the tree in post-order.
        Return 1) if p or q is found in the sub-tree
           and 2) the dist from p or q to the current node (if found).
        """
        @lru_cache(None)
        def traverse(node, p, q):
            """Traverse the tree post-order."""
            nonlocal res
            if not node:
                return False, -inf
            lfound, left = traverse(node.left, p, q)
            rfound, right = traverse(node.right, p, q)

            if node.val in (p, q) or lfound and rfound:
                if lfound:
                    res += left + 1
                if rfound:
                    res += right + 1
                return True, 0
            return left or rfound, max(left, right) + 1

        res = 0
        traverse(root)
        return res


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        236. Lowest Common Ancestor of a Binary Tree
        1644. Lowest Common Ancestor of a Binary Tree II
        (If either node p or q does not exist in the tree, return null.)
        BFS traverse the tree from root and keep track of {node.val: parent}
        The idea is simmilar with 1257, first traverse the tree from root and record
        each node's parent, then start from p, traverse the through parents and use a
        set to record all ancesters.
        O(N) space, O(N) time
        """
        parents = {root.val: None}
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parents[node.left.val] = node
                queue.append(node.left)
            if node.right:
                parents[node.right.val] = node
                queue.append(node.right)

        if p.val not in parents or q.val not in parents:
            return None

        ancestors = set()
        while p:
            ancestors.add(p.val)
            p = parents[p.val]
        while q and q.val not in ancestors:
            q = parents[q.val]
        return q


class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        """
        1650. Lowest Common Ancestor of a Binary Tree III
        NOTES: we don't know root of the tree.
        But we know the parent of each node
        All Node.val are UNIQUE.
        O(H) Time and Space
        """
        ancestors = set()
        while p:
            ancestors.add(p)
            p = p.parent
        while q and q not in ancestors:
            q = q.parent
        return q


class Solution:
    def findSmallestRegion(self, regions: List[List[str]], p: str, q: str) -> str:
        """
        1257. Smallest Common Region
        Given two regions p and q, return the smallest region containing both.
        """
        parent = dict()
        for region in regions:
            for x in region[1:]:
                parent[x] = region[0]

        chain = set([p])
        while p in parent:
            p = parent[p]
            chain.add(p)
        while q not in chain:
            q = parent[q]
        return q


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        160. Intersection of Two Linked Lists
        """
        nodes = set()
        p, q = headA, headB
        while p:
            nodes.add(p)
            p = p.next
        while q and q not in nodes:
            q = q.next
        return q


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        160. Intersection of Two Linked Lists
        """
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p


class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        """
        1650. Lowest Common Ancestor of a Binary Tree III
        NOTES: we don't know root of the tree.
        But we know the parent of each node
        x points to root -> x.parent is None
        This soluiton is the same as finding the convergence point of 2 linked lists.
        We keep two pointers, x and y. Originally, these pointers point to q and p,
        respectively. Then we follow their parent pointers until they point to the same
        node. When either of the pointers points to root, we set it to the other original
        starting node. For example, when x points to root (i.e x.parent is None),
        assign q to x.
        """
        x, y = p, q
        while x != y:
            x = x.parent if x.parent else q
            y = y.parent if y.parent else p
        return x


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        1650. Lowest Common Ancestor of a Binary Tree III
        """
        def getDepth(node):
            depth = 0
            while node.parent:
                node = node.parent
                depth += 1
            return depth

        dp, dq = getDepth(p), getDepth(q)
        if dp < dq:
            for _ in range(dq - dp):
                q = q.parent
        else:
            for _ in range(dp - dq):
                p = p.parent
        # now p and q are the same level
        while p != q:
            p = p.parent
            q = q.parent
        return p


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        """
        1198. Find Smallest Common Element in All Rows
        Each row is sorted in strictly increasing order.
        Return the smallest common element in all rows.
        Solution1 : use intersection of set
        """
        nums = set(mat[0])
        for row in mat[1:]:
            nums = nums & set(row)
        return min(nums) if nums else -1


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        """
        1198. Find Smallest Common Element in All Rows
        Each row is sorted in strictly increasing order.
        Return the smallest common element in all rows.
        Solution1 : use a frequency table, and scan top-down
        """
        M, N = len(mat), len(mat[0])
        freq = defaultdict(int)
        for j, i in product(range(N), range(M)):
            freq[mat[i][j]] += 1
            if freq[mat[i][j]] == M:
                return mat[i][j]
        return -1
