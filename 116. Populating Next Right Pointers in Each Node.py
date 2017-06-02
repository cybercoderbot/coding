# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        
        # 这道题实际上是树的层序遍历的应用，既然是遍历，就有递归和非递归两种方法，最好两种方法都要掌握，
        # 都要会写。下面先来看递归的解法，由于是完全二叉树，所以若节点的左子结点存在的话，其右子节点必定
        # 存在，所以左子结点的next指针可以直接指向其右子节点，对于其右子节点的处理方法是，判断其父节点的
        # next是否为空，若不为空，则指向其next指针指向的节点的左子结点，若为空则指向None
        
        if not root: return
        if root.left:
            root.left.next = root.right
        if root.right:
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None
            
        self.connect(root.left)
        self.connect(root.right)
        
        
        
