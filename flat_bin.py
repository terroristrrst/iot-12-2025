class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_view(root):
    if not root:
        return []
    
    queue = [(root, 0)]
    col_map = {}
    
    while queue:
        node, x = queue.pop(0)
        if x not in col_map:
            col_map[x] = []
        col_map[x].append(node.val)
        
        if node.left:
            queue.append((node.left, x - 1))
        if node.right:
            queue.append((node.right, x + 1))
    
    result = []
    for x in sorted(col_map.keys()):
        result.extend(col_map[x])
    return result

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)
root.left.left.left = TreeNode(1)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(8)

view = vertical_view(root)
print(view)
print(''.join(map(str, view)))
