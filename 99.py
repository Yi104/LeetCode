class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)
        
        nodes = inorder_traversal(root)
        swapped = []
        prev = None
        
        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i + 1].val:
                swapped.append(nodes[i])
                swapped.append(nodes[i + 1])
        
        if swapped:
            swapped[0].val, swapped[-1].val = swapped[-1].val, swapped[0].val
