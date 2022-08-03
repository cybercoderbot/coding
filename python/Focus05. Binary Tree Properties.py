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

        queue = [(root, -inf, inf)]
        while queue:
            node, low, high = queue.pop(0)
            if low >= node.val or high <= node.val:
                return False
            if node.left:
                queue.append((node.left, low, node.val))
            if node.right:
                queue.append((node.right, node.val, high))
        return True


class Solution:
    """
    101. Symmetric Tree
    """

    def isReflective(self, t1, t2) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False

        left = self.isReflective(t1.left, t2.right)
        right = self.isReflective(t1.right, t2.left)
        return left and right

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Recursive Solution"""
        return self.isReflective(root, root)


class Solution:
    def isSymmetric(self, root):
        """
        101. Symmetric Tree
        """
        if root is None:
            return True
        queue = [(root.left, root.right)]
        while queue:
            left, right = queue.pop(0)
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        111. Minimum Depth of Binary Tree
        """
        if not root:
            return 0

        queue = [(root, 1)]
        while queue:
            node, depth = queue.pop(0)
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

        queue = [(root, 1)]
        while queue:
            node, depth = queue.pop(0)
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

        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                queue.extend((node.left, node.right))
        return root


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
        """ 257. Binary Tree Paths (get all root-to-leaf paths) """
        if not root:
            return []

        paths = []
        queue = [(root, str(root.val))]
        while queue:
            node, path = queue.pop(0)
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

        def closet(x):
            nonlocal target
            return abs(x-target)

        node = root
        res = inf
        while node:
            res = min(res, node.val, key=closet)
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

        def closet(x):
            nonlocal target
            return abs(x-target)

        nums = postorder(root)
        nums.sort(key=closet)
        return nums[:k]


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
        queue = [(root, 1)]
        while queue:
            node, leng = queue.pop(0)
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
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        """
        366. Find Leaves of Binary Tree
        seen: {heights : [nodes]}
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
    def findMode(self, root: TreeNode) -> List[int]:
        """
        501. Find Mode in Binary Search Tree
        """
        if not root:
            return

        queue = [root]
        freq = defaultdict(int)
        while queue:
            node = queue.pop(0)
            freq[node.val] += 1
            if node.left:
                queue.append((node.left))
            if node.right:
                queue.append((node.right))

        fmax = max(freq.values())
        return [key for key, val in freq.items() if val == fmax]


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        543. Diameter of Binary Tree (longest path between any 2 nodes)
        """
        @lru_cache(None)
        def traverse(node):
            """Compute height of the tree"""
            nonlocal res
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            res = max(res, left+right)
            return max(left, right) + 1

        res = 0
        traverse(root)
        return res


class Solution:
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
        def traverse(node):
            """Return tree's nodes sum"""
            nonlocal res
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            res += abs(left - right)
            return left + right + node.val

        res = 0
        traverse(root)
        return res


class Solution:
    def isSameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not (s and t):
            return s == t
        left = self.isSameTree(s.left, t.left)
        right = self.isSameTree(s.right, t.right)
        return s.val == t.val and left and right

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
        Inorder traverse the tree and construct string
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
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        617. Merge Two Binary Trees
        """
        if not root1 or not root2:
            return root1 or root2
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
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
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val == k:
                src = node
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        queue, seen = [src], {src}
        while queue:
            node = queue.pop(0)
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
        queue = [root]
        while queue:
            node = queue.pop(0)
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
    def isUnivalTree(self, root: TreeNode) -> bool:
        """
        965. Univalued Binary Tree (all nodes have the same val)
        Inorder traverse the tree. If len(seen) > 1: return False
        """
        seen = set()
        queue = [root]
        while queue:
            node = queue.pop(0)
            seen.add(node.val)
            if len(values) > 1:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True


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
        queue = [(root, -inf)]
        while queue:
            node, high = queue.pop(0)
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
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """1650. Lowest Common Ancestor of a Binary Tree III"""
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1 else q
            p2 = p2.parent if p2 else p
        return p1

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
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
