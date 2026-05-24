class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binary_tree_diameter(tree: BinaryTree) -> int:
    max_diameter = [0]

    def dfs(node):
        if not node:
            return -1 
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        
        if node.left and node.right:
            max_diameter[0] = max(max_diameter[0], left_height + right_height + 2)
        return 1 + max(left_height, right_height)

    dfs(tree)
    return max_diameter[0]
