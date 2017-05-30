# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        # 这道题要求把二叉树展开成链表，根据展开后形成的链表的顺序分析出是使用先序遍历，
        # 那么只要是数的遍历就有递归和非递归的两种方法来求解，这里我们也用两种方法来求解。
        # 下面我们再来看非迭代版本的实现，这个方法是从根节点开始出发，先检测其左子结点是否存在，
        # 如存在则将根节点和其右子节点断开，将左子结点及其后面所有结构一起连到原右子节点的位置，
        # 把原右子节点连到元左子结点最后面的右子节点之后。
        
        # Non-recursive preorder traversal
        # in the flattened tree, each node's right child points to the next node of a pre-order traversal.
        current = TreeNode(None)
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                current.right = node
                current.left = None
                current = node
                
                
                
