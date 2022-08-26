class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        98. Validate Binary Search Tree
        Inorder traverse BST -> nums sorted in ascending order
        """
        @lru_cache(None)
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        nums = []
        inorder(root)
        return all(x < y for x, y in zip(nums[:-1], nums[1:]))


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        98. Validate Binary Search Tree
        BFS traverse BST -> keep track of low and high bounds
        """
        if not root:
            return True

        queue = collections.deque([(root, -inf, inf)])
        while queue:
            node, low, high = queue.popleft()
            if low >= node.val or high <= node.val:
                return False
            if node.left:
                queue.append((node.left, low, node.val))
            if node.right:
                queue.append((node.right, node.val, high))
        return True


class Solution:
    def isReflective(self, t1, t2) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2 or t1.val != t2.val:
            return False
        left = self.isReflective(t1.left, t2.right)
        right = self.isReflective(t1.right, t2.left)
        return left and right

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        101. Symmetric Tree (Recursive Solution)
        """
        return self.isReflective(root, root)


class Solution:
    def isSymmetric(self, root):
        """
        101. Symmetric Tree
        """
        if root is None:
            return True
        queue = collections.deque([(root.left, root.right)])
        while queue:
            left, right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True


class Solution:
    @lru_cache(None)
    def height(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return max(left, right) + 1

    @lru_cache(None)
    def isBalanced(self, root: TreeNode) -> bool:
        """
        110. Balanced Binary Tree (max diff <=1 between any 2 nodes)
        """
        if not root:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        x, y = self.height(root.left), self.height(root.right)
        return left and right and abs(x - y) <= 1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        110. Balanced Binary Tree (max diff <=1 between any 2 nodes)
        Post-order traverse the tree. left -> right -> root
        At each node, collect the info if its left and right subtrees are
        balanced and their height.
        Time: O(N), Space: O(N)
        """
        @lru_cache(None)
        def check(node):
            """Return if tree is balanced and its height."""
            if not node:
                return True, 0

            left, height1 = check(node.left)
            right, height2 = check(node.right)

            height = max(height1, height2) + 1
            balanced = left and right and abs(height1 - height2) <= 1

            return balanced, height

        res, _ = check(root)

        return res


class Solution:
    @lru_cache(None)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        111. Minimum Depth of Binary Tree
        """
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return min(left, right) + 1


class Solution:
    @lru_cache(None)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        104. Maximum Depth of Binary Tree
        """
        if not root:
            return 0
        if not root.left:
            return self.maxDepth(root.right) + 1
        if not root.right:
            return self.maxDepth(root.left) + 1

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


class Solution:
    @lru_cache(None)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        104. Maximum Depth of Binary Tree
        """
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        111. Minimum Depth of Binary Tree
        """
        if not root:
            return 0

        depth, queue = 1, [root]
        while queue:
            level = []
            for node in queue:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level
            depth += 1

        return depth


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        111. Minimum Depth of Binary Tree
        """
        if not root:
            return 0

        queue = collections.deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return 0


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        104. Maximum Depth of Binary Tree
        """
        if not root:
            return 0

        queue = collections.deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return depth


class Solution:
    @lru_cache(None)
    def flatten(self, root: TreeNode) -> None:
        """
        114. Flatten Binary Tree to Linked List
        root: [1,2,5,3,4,null,6]
        output: [1,null,2,null,3,null,4,null,5,null,6]
        """
        if not root:
            return None
        if not root.left and not root.right:
            return root

        left = self.flatten(root.left)
        right = self.flatten(root.right)
        if left:
            left.right = root.right
            root.right = root.left
            root.left = None

        # return the rightmost node
        return right if right else left


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        124. Binary Tree Maximum Path Sum
        Post order traverse
        """
        @lru_cache(None)
        def pathSum(node):
            """Returns max path starting at node"""
            if not node:
                return 0
            left = max(pathSum(node.left), 0)
            right = max(pathSum(node.right), 0)
            paths.append(left + node.val + right)
            return max(left, right) + node.val

        paths = []
        pathSum(root)
        return max(paths)


class Solution:
    @lru_cache(None)
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        """
        156. Binary Tree Upside Down
        1) The original left child becomes the new root.
        2) The original root becomes the new right child.
        3) The original right child becomes the new left child.
        """
        if not root or not root.left:
            return root
        node = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None
        return node


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        199. Binary Tree Right Side View
        """
        if not root:
            return []

        res = []
        queue = [root]
        while queue:
            qnext = []
            for node in queue:
                if node.left:
                    qnext.append(node.left)
                if node.right:
                    qnext.append(node.right)
            # The current level is finished.
            # The last element is the rightmost one.
            res.append(node.val)
            queue = qnext
        return res


class Solution:
    @lru_cache(None)
    def countNodes(self, root: TreeNode) -> int:
        """
        222. Count Nodes of Complete Binary Tree
        Time: O(N), Space: O(d) = O(logN). d = tree depth.
        Count nodes recursively one by one.
        """
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left + right + 1


class Solution:
    @lru_cache(None)
    def countNodes(self, root: TreeNode) -> int:
        """
        222. Count Nodes of Complete Binary Tree
        """
        if not root:
            return 0

        def depth(node):
            if not node:
                return 0
            return depth(node.left) + 1

        left = depth(root.left)
        right = depth(root.right)
        if left == right:
            return pow(2, left) + self.countNodes(root.right)
        elif left > right:
            return self.countNodes(root.left) + pow(2, right)


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        """
        270. Closest Binary Search Tree Value
        Return the value that is closest to the target
        """
        if not root:
            return 0

        res = inf
        node = root
        while node:
            res = min(res, node.val, key=lambda x: abs(x-target))
            if node.val < target:
                node = node.right
            else:
                node = node.left
        return res


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        """
        272. Closest Binary Search Tree Value II
        Return the k values that are closest to the target
        """
        def inorder(node: TreeNode):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        def preorder(node: TreeNode):
            if not node:
                return []
            return [node.val] + preorder(node.left) + preorder(node.right)

        def postorder(node: TreeNode):
            if not node:
                return []
            return postorder(node.left) + postorder(node.right) + [node.val]

        nums = preorder(root)
        nums.sort(key=lambda x: abs(x-target))
        return nums[:k]


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        """
        250. Count Univalue Subtrees
        """
        @lru_cache(None)
        def isUnival(node, parent):
            """True if a tree is unival"""
            nonlocal res
            if not node:
                return True
            left = isUnival(node.left, node.val)
            right = isUnival(node.right, node.val)
            if left and right:
                res += 1
            return left and right and node.val == parent

        res = 0
        isUnival(root, None)
        return res


class Solution:
    @lru_cache(None)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ 226. Invert Binary Tree (flip left <-> right) """
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ 226. Invert Binary Tree (flip left <-> right) """
        if not root:
            return None

        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.extend((node.left, node.right))
        return root


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        230. Kth Smallest Element in a BST
        Inorder traverse: node val sorted in ascending order
        """
        @lru_cache(None)
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        nums = []
        inorder(root)
        return nums[k-1]


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        230. Kth Smallest Element in a BST
        Inorder traverse: node val sorted in ascending order
        """
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        235. Lowest Common Ancestor of a Binary Search Tree
        """
        if p.val > q.val:
            p, q = q, p

        node = root
        while node:
            if node.val < p.val:
                node = node.right
            elif p.val <= node.val <= q.val:
                return node
            else:
                node = node.left


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        235. Lowest Common Ancestor of a Binary Search Tree
        """
        if not root:
            return None

        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node


class Solution:
    @lru_cache(None)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        236. Lowest Common Ancestor of a Binary Tree
        """
        if not root or root in (p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """
        257. Binary Tree Paths (get all root-to-leaf paths)
        """
        if not root:
            return []

        paths = []
        queue = collections.deque([(root, str(root.val))])
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                queue.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                queue.append((node.right, path + '->' + str(node.right.val)))
        return paths


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        """
        270. Closest Binary Search Tree Value
        """
        if not root:
            return 0

        def dist(x):
            nonlocal target
            return abs(x-target)

        node = root
        res = inf
        while node:
            res = min(res, node.val, key=dist)
            if node.val < target:
                node = node.right
            else:
                node = node.left
        return res


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        """
        272. Closest Binary Search Tree Value II
        Return the k values in the BST that are closest to the target
        """
        @lru_cache(None)
        def preorder(node: TreeNode):
            if not node:
                return []
            return [node.val] + preorder(node.left) + preorder(node.right)

        @lru_cache(None)
        def inorder(node: TreeNode):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        @lru_cache(None)
        def postorder(node: TreeNode):
            if not node:
                return []
            return postorder(node.left) + postorder(node.right) + [node.val]

        def dist(x):
            nonlocal target
            return abs(x-target)

        nums = postorder(root)
        nums.sort(key=dist)
        return nums[:k]


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        """
        285. Inorder Successor in BST
        """
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor


class Solution:
    @lru_cache(None)
    def inorderSuccessor(self, root: TreeNode, p: TreeNode, last=None) -> Optional[TreeNode]:
        """
        285. Inorder Successor in BST
        """
        if not root:
            return last
        if p.val < root.val:
            return self.inorderSuccessor(root.left, p, root)
        else:
            return self.inorderSuccessor(root.right, p, last)


class Solution:
    def isLeaf(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])
        return all(grid[i][j] == grid[0][0] for i, j in product(range(M), range(N)))

    def construct(self, grid: List[List[int]]) -> Node:
        """
        427. Construct Quad Tree
        """
        if not grid:
            return None
        if self.isLeaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)

        root = Node()
        root.isLeaf = False
        x = len(grid) // 2
        root.topLeft = self.construct([row[:x] for row in grid[:x]])
        root.topRight = self.construct([row[x:] for row in grid[:x]])
        root.bottomLeft = self.construct([row[:x] for row in grid[x:]])
        root.bottomRight = self.construct([row[x:] for row in grid[x:]])
        return root


class Solution:
    def inorderSuccessor(self, node: TreeNode) -> TreeNode:
        """
        510. Inorder Successor in BST II
        Difference to 285: you will have direct access to the node but
        not to the root of the tree. Each node will have a ref to its parent node.
        """
        # the successor is somewhere lower in the right subtree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        # the successor is somewhere upper in the tree
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        530. Minimum Absolute Difference in BST
        Inorder traverse: nums sorted in ascending order
        """
        @lru_cache(None)
        def inorder(node):
            if node.left:
                inorder(node.left)
            nums.append(node.val)
            if node.right:
                inorder(node.right)
            return

        nums = []
        inorder(root)
        res = min(y-x for x, y in zip(nums[:-1], nums[1:]))
        return res


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        530. Minimum Absolute Difference in BST
        """
        @lru_cache(None)
        def traverse(node, low, high):
            if not node:
                return high - low

            left = traverse(node.left, low, node.val)
            right = traverse(node.right, node.val, high)
            return min(left, right)

        res = traverse(node=root, low=-inf, high=inf)
        return res


class Solution:
    @lru_cache(None)
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        """
        671. Second Minimum Node In a Binary Tree
        root.val = min(root.left.val, root.right.val) always holds.
        Root node is the smallest node in the tree. 
        We just have to recursively traverse the tree and find a node that is bigger than 
        the root but smaller than any existing node we have come across.
        """
        if not root.left or not root.right:
            return -1

        left, right = root.left.val, root.right.val
        if root.left.val == root.val:
            left = self.findSecondMinimumValue(root.left)
        if root.right.val == root.val:
            right = self.findSecondMinimumValue(root.right)

        if left != -1 and right != -1:
            return min(left, right)
        else:
            return max(left, right)


class Solution:
    @lru_cache(None)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        938. Range Sum of BST
        """
        if not root:
            return 0

        res = 0
        if root.val > low:
            res += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            res += self.rangeSumBST(root.right, low, high)
        if low <= root.val <= high:
            res += root.val
        return res


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        993. Cousins in Binary Tree
        Preorder DFS iteration and record depth and parent of each node
        queue: (node, depth, parent)
        seen[node] = (depth, parent)
        cousin: same depth, different parents
        """
        if not root:
            return False

        seen = defaultdict(tuple)
        queue = collections.deque([(root, 0, None)])
        while queue:
            node, depth, parent = queue.popleft()
            if not node:
                continue
            if node.val in (x, y):
                seen[node.val] = (depth, parent)
            queue.append((node.left, depth+1, node))
            queue.append((node.right, depth+1, node))

        depthx, parentx = seen[x]
        depthy, parenty = seen[y]
        return depthx == depthy and parentx != parenty


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        """
        298. Binary Tree Longest Consecutive Sequence
        Traverse the tree using stack and keep track of longest consec seq
        Time: O(N), Space: O(N)
        """
        if not root:
            return 0

        res = 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, leng = queue.popleft()
            llen = rlen = leng
            res = max(res, leng)
            if node.left:
                if node.left.val != node.val + 1:
                    llen = 0
                queue.append((node.left, llen+1))
            if node.right:
                if node.right.val != node.val + 1:
                    rlen = 0
                queue.append((node.right, rlen+1))
        return res


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        """
        333. Largest BST Subtree
        """
        @lru_cache(None)
        def traverse(node):
            """
            Post order traverse the tree
            Return a few parameters of sub-tree rooted at node.
            isBST? | size | low | high
            """
            nonlocal res

            if not node:
                return True, 0, inf, -inf

            valid1, size1, low1, high1 = traverse(node.left)
            valid2, size2, low2, high2 = traverse(node.right)

            valid = valid1 and valid2 and high1 < node.val < low2
            size = size1 + size2 + 1
            if valid:
                res = max(res, size)

            low = min(low1, node.val)
            high = max(node.val, high2)

            return valid, size, low, high

        res = 0
        traverse(root)
        return res


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:

        @lru_cache(None)
        def traverse(node):
            """
            Collect info while traversing the tree in post-order.
            isBST? | low | high | sum | maxSum
            """
            if not node:
                return True, inf, -inf, 0, 0

            valid1, low1, high1, sum1, left = traverse(node.left)
            valid2, low2, high2, sum2, right = traverse(node.right)
            low1 = min(low1, node.val)
            high2 = max(high2, node.val)
            sm = sum1 + sum2 + node.val
            if valid1 and valid2 and high1 < node.val < low2:
                return True, low1, high2, sm, max(left, right, sm)
            return False, low1, high2, sm, max(left, right)

        res = traverse(root)
        return res[-1]


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        """
        366. Find Leaves of Binary Tree
        seen: {heights (bottom up): [nodes]}
        """
        def traverse(node):
            """Return height of give node"""
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            height = max(left, right) + 1
            seen[height].append(node.val)
            return height

        seen = defaultdict(list)
        traverse(root)
        return seen.values()


class Solution:
    @lru_cache(None)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        404. Sum of Left Leaves
        """
        def isLeaf(node):
            return node and not node.left and not node.right

        if not root:
            return 0
        if isLeaf(root.left):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)
        return left + right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        404. Sum of Left Leaves
        """
        def isLeaf(node):
            return node and not node.left and not node.right

        res = 0
        queue = collections.deque([(root, False)])
        while queue:
            node, isLeft = queue.popleft()
            if isLeft and isLeaf(node):
                res += node.val
            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))
        return res


class Solution:
    @lru_cache(None)
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        450. Delete Node in a BST
        """
        if not root:
            return None

        if root.val == key:
            if not root.left or not root.right:
                return root.right or root.left

            node = root.right
            while node.left:
                node = node.left
            root.val = node.val
            root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        """
        508. Most Frequent Subtree Sum
        """
        def treeSum(node):
            """Populate frequency table."""
            if not node:
                return 0
            sm = node.val + treeSum(node.left) + treeSum(node.right)
            freq[sm] += 1
            return sm

        freq = defaultdict(int)
        treeSum(root)
        return [k for k, v in freq.items() if v == max(freq.values())]


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        426. Convert Binary Search Tree to Sorted Doubly Linked List
        """
        if not root:
            return None

        def flatten(node):
            """Return head & tail of flattened tree."""
            head = tail = node
            if node.left:
                head, tail0 = flatten(node.left)
                tail0.right = node
                node.left = tail0
            if node.right:
                head1, tail = flatten(node.right)
                node.right = head1
                head1.left = node
            return head, tail

        head, tail = flatten(root)
        head.left = tail
        tail.right = head
        return head


class Solution:
    @lru_cache(None)
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        1325. Delete Leaves With a Given Value
        Post order traverse the tree and remove leaves
        """
        def isLeaf(node):
            return node and not node.left and not node.right

        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if isLeaf(root) and root.val == target:
            return None
        return root


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """
        1302. Deepest Leaves Sum of binary tree
        """
        if not root:
            return 0
        res = 0
        queue = [root]
        while queue:
            total, level = 0, []
            for node in queue:
                total += node.val
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            res = total
            queue = level
        return res


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        1530. Number of Good Leaf Nodes Pairs
        A pair of two different leaf nodes of a binary tree is said to be good 
        if the length of the shortest path between them is <= distance.
        Return the number of good leaf node pairs in the tree.
        """
        @lru_cache(None)
        def node2LeafDists(node):
            """The list of distance of the leaf nodes to each node."""
            nonlocal res
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = node2LeafDists(node.left)
            right = node2LeafDists(node.right)
            res += sum(x+y <= distance for x in left for y in right)
            return [d+1 for d in left+right if d+1 < distance]

        res = 0
        node2LeafDists(root)
        return res


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        """
        501. Find Mode in Binary Search Tree
        """
        if not root:
            return

        queue = collections.deque([root])
        freq = defaultdict(int)
        while queue:
            node = queue.popleft()
            freq[node.val] += 1
            if node.left:
                queue.append((node.left))
            if node.right:
                queue.append((node.right))

        fmax = max(freq.values())
        return [key for key, val in freq.items() if val == fmax]


class Solution:
    def leafSimilar(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        """
        872. Leaf-Similar Trees
        Return true if the two trees root1 and root2 are leaf-similar.
        """
        @lru_cache(None)
        def findLeaf(root: TreeNode) -> List[int]:
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            left = findLeaf(root.left)
            right = findLeaf(root.right)
            return left + right

        return findLeaf(t1) == findLeaf(t2)


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        543. Diameter of Binary Tree (longest path between any 2 nodes)
        """
        @lru_cache(None)
        def height(node):
            """Compute height of the tree"""
            nonlocal res
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            res = max(res, left+right)
            return max(left, right) + 1

        res = 0
        height(root)
        return res


class Solution:
    @lru_cache(None)
    def getLeaves(self, node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        return self.getLeaves(node.left) + self.getLeaves(node.right)

    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        """
        545. Boundary of Binary Tree
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        left = []
        node = root.left
        while node:
            left.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right

        right = []
        node = root.right
        while node:
            right.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left

        # trim last leaf node leaf
        left = left[:-1]
        right = right[:-1]
        leaves = self.getLeaves(root)

        # don't forget to reverse right
        return [root.val] + left + leaves + right[::-1]


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        """
        549. Binary Tree Longest Consecutive Sequence II
        Path could be child-Parent-child, not necessarily parent-child.
        """
        @lru_cache(None)
        def traverse(node):
            """
            Post-order traverse tree
            Return longest inc & dec seqs starting at node
            """
            nonlocal res
            if not node:
                return 0, 0

            inc1, dec1 = traverse(node.left)
            inc2, dec2 = traverse(node.right)
            inc = dec = 1
            if node.left:
                if node.left.val + 1 == node.val:
                    inc = inc1 + 1
                elif node.left.val - 1 == node.val:
                    dec = dec1 + 1
            if node.right:
                if node.right.val + 1 == node.val:
                    inc = max(inc, inc2 + 1)
                elif node.right.val - 1 == node.val:
                    dec = max(dec, dec2 + 1)

            res = max(res, inc + dec - 1)
            return inc, dec

        res = 0
        traverse(root)
        return res


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        """
        563. Binary Tree Tilt (abs diff of sum(left) and sum(right))
        Postorder traverse tree and keep track of max diff
        """
        @lru_cache(None)
        def treeSum(node):
            """Return tree's nodes sum"""
            nonlocal res
            if not node:
                return 0
            left = treeSum(node.left)
            right = treeSum(node.right)
            res += abs(left - right)
            return left + right + node.val

        res = 0
        treeSum(root)
        return res


class Solution:
    @lru_cache(None)
    def isSameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s or not t:
            return s == t
        if s.val != t.val:
            return False
        left = self.isSameTree(s.left, t.left)
        right = self.isSameTree(s.right, t.right)
        return left and right

    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        """572. Subtree of Another Tree"""
        if not s:
            return False
        if self.isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


class Solution:
    @lru_cache(None)
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        606. Construct String from Binary Tree
        [1,2,3,4] -> "1(2(4))(3)"
        Preorder traverse the tree and construct string
        """
        if not root:
            return ""

        res = str(root.val)
        if not root.left and root.right:
            res += "()"
        if root.left:
            res += "(" + self.tree2str(root.left) + ")"
        if root.right:
            res += "(" + self.tree2str(root.right) + ")"
        return res


class Solution:
    @lru_cache(None)
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        617. Merge Two Binary Trees
        """
        if not t1 or not t2:
            return t2 or t1
        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        637. Average of Levels in Binary Tree
        """
        if not root:
            return []

        queue, res = [root], []
        while queue:
            vals, level = [], []
            for node in queue:
                vals.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            res.append(sum(vals)/len(vals))
            queue = level
        return res


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        654. Maximum Binary Tree
        Brute force O(N^2) solution
        """
        if not nums:
            return
        i = nums.index(max(nums))
        left = self.constructMaximumBinaryTree(nums[:i])
        right = self.constructMaximumBinaryTree(nums[i+1:])
        return TreeNode(nums[i], left, right)


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        654. Maximum Binary Tree
        Stack O(N) solution
        """
        stack = []
        for x in nums:
            node = TreeNode(x)
            while stack and stack[-1].val < x:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        662. Maximum Width of Binary Tree
        BFS level order traverse tree. Keep track of max width
        """
        if not root:
            return 0

        res = 0
        queue = [(root, 0)]
        while queue:
            left, right = queue[0], queue[-1]
            res = max(res, right[1] - left[1] + 1)
            level = []
            for node, x in queue:
                if node.left:
                    level.append((node.left, 2*x))
                if node.right:
                    level.append((node.right, 2*x+1))
            queue = level
        return res


class Solution:
    @lru_cache(None)
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        """
        669. Trim a Binary Search Tree
        """
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root


class Solution:
    @lru_cache(None)
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        700. Search in a Binary Search Tree
        Find the node in the BST that the node's value equals val
        """
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        """
        742. Closest Leaf in a Binary Tree to node of val k
        """
        parent = {root: None}
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.val == k:
                src = node
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        queue, seen = collections.deque([src]), {src}
        while queue:
            node = queue.popleft()
            if not node.left and not node.right:
                return node.val
            for p in (node.left, node.right, parent[node]):
                if p and p not in seen:
                    queue.append(p)
                    seen.add(p)


class Solution:
    @lru_cache(None)
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        814. Binary Tree Pruning (prune subtree that doesn't contain 1)
        """
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and not root.val:
            return None
        return root


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


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        """
        965. Univalued Binary Tree (all nodes have the same val)
        Inorder traverse the tree. If len(seen) > 1: return False
        """
        if not root:
            return True

        seen = set()
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            seen.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return len(seen) == 1


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        538. Convert BST to Greater Tree
        1038. Binary Search Tree to Greater Sum Tree
        Reversed inorder traverse: right->root->left
        """
        @lru_cache(None)
        def reversedInorder(node: TreeNode, pre: int) -> int:
            """Return gst node val"""
            if not node:
                return pre
            right = reversedInorder(node.right, pre)
            node.val += right
            res = reversedInorder(node.left, node.val)
            return res

        reversedInorder(node=root, pre=0)
        return root


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
        1245. Tree Diameter
        """
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
                for p in queue:
                    for q in connected[p]:
                        if q not in seen:
                            qnext.append(q)
                            seen.add(q)
                queue = qnext
                level += 1
            return p, level - 1

        # two passes
        # 1st pass - find a node on longest path
        # 2nd pass - find longest path (tree diameter)
        node = bfs(0)[0]
        return bfs(node)[1]


class Solution:
    def getAllElements(self, root1, root2):
        """
        Before you scream "But sorting isn't linear!", know that
        Timsort, which identifies the 2 already sorted runs and merges them.
        """
        @lru_cache(None)
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
            return

        nums = []
        inorder(root1)
        inorder(root2)
        return sorted(nums)


class Solution:
    @lru_cache(None)
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """"
        1367. Linked List in Binary Tree
        Time O(N * min(L,H)), Space O(H)
        where N = tree size, H = tree height, L = list length.
        """
        @lru_cache(None)
        def sub(head, root):
            if not head:
                return True
            if not root:
                return False
            if root.val != head.val:
                return False
            left = sub(head.next, root.left)
            right = sub(head.next, root.right)
            return left or right

        if not head:
            return True
        if not root:
            return False

        left = self.isSubPath(head, root.left)
        right = self.isSubPath(head, root.right)
        return sub(head, root) or left or right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        1339. Maximum Product of Splitted Binary Tree
        Postorder traverse of the tree
        """
        @lru_cache(None)
        def sumOfNodes(node):
            """Return sum of subtree."""
            if not node:
                return 0
            left = sumOfNodes(node.left)
            right = sumOfNodes(node.right)
            res = node.val + left + right
            nums.append(res)
            return res

        nums = []
        total = sumOfNodes(root)
        products = [(total-x)*x for x in nums]
        return max(products) % 1_000_000_007


class Solution:
    @lru_cache(None)
    def sumNumbers(self, root: TreeNode, pre=0) -> int:
        """
        129. Sum Root to Leaf Numbers
        root = [1,2,3] -> 25
        """
        def isLeaf(node):
            return node and not node.left and not node.right

        if not root:
            return 0
        pre = 10 * pre + root.val
        if isLeaf(root):
            return pre

        left = self.sumNumbers(root.left, pre)
        right = self.sumNumbers(root.right, pre)
        return left + right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        129. Sum Root to Leaf Numbers (root = [1,2,3] -> 25)
        BFS for level order traverse
        Record (node, pre) when traversing the tree
        res += pre when reaching leaf node
        """
        def isLeaf(node):
            return node and not node.left and not node.right
        queue = collections.deque([(root, 0)])
        res = 0
        while queue:
            node, pre = queue.popleft()
            pre = 10 * pre + node.val
            if isLeaf(node):
                res += pre
            if node.left:
                queue.append((node.left, pre))
            if node.right:
                queue.append((node.right, pre))
        return res


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        1382. Balance a Binary Search Tree
        root = [1,null,2,null,3,null,4,null,null]
        res: [2,1,3,null,null,null,4]
        Traverse binary tree in-order to get sorted array
        The problem become 108. Convert Sorted Array to Binary Search Tree
        """
        @lru_cache(None)
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
            return

        def build(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = build(nums[:mid])
            root.right = build(nums[mid + 1:])
            return root

        nums = []
        inorder(root)
        return build(nums)


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        1448. Count Good Nodes in Binary Tree
        Good node: root->X all nodes are smaller than X.
        """
        if not root:
            return 0

        res = 0
        queue = collections.deque([(root, -inf)])
        while queue:
            node, high = queue.popleft()
            if node.val >= high:
                res += 1
            high = max(high, node.val)
            if node.left:
                queue.append((node.left, high))
            if node.right:
                queue.append((node.right, high))
        return res


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        1448. Count Good Nodes in Binary Tree
        Good node: root->X all nodes are smaller than X.
        """
        @lru_cache(None)
        def traverse(node, high):
            if not node:
                return 0
            isGood = node.val >= high
            high = max(high, node.val)
            left = traverse(node.left, high)
            right = traverse(node.right, high)
            res = isGood + left + right
            return res

        return traverse(node=root, high=root.val)


class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        """1650. Lowest Common Ancestor of a Binary Tree III"""
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1 else q
            p2 = p2.parent if p2 else p
        return p1

    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        """1650. Lowest Common Ancestor of a Binary Tree III"""
        seen = set()
        while q:
            seen.add(q.val)
            q = q.parent
        while p:
            if p.val in seen:
                return p
            seen.add(p.val)
            p = p.parent
        return None


class Solution:
    @lru_cache(None)
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
        2331. Evaluate Boolean Binary Tree
        Leaf nodes: 0 or 1. 0: False, 1: True.
        Non-leaf nodes: 2 or 3. 2: boolean OR,  3 boolean AND.
        Post-order traverse the tree and evaluate at each level
        """
        if root.val in (0, 1):
            return bool(root.val)

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        if root.val == 2:
            return left or right
        elif root.val == 3:
            return left and right
