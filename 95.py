class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateTrees(n):
    if n == 0:
        return []
    return generate_trees_helper(1, n)

def generate_trees_helper(start, end):
    if start > end:
        return [None]
    
    result = []
    for i in range(start, end + 1):
        left_subtrees = generate_trees_helper(start, i - 1)
        right_subtrees = generate_trees_helper(i + 1, end)
        
        for left in left_subtrees:
            for right in right_subtrees:
                root = TreeNode(i)
                root.left = left
                root.right = right
                result.append(root)
    
    return result
