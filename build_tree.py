class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_array(arr):
    if not arr or arr[0] is None:
        return None
    nodes = [None if val is None else TreeNode(val) for val in arr]
    for i in range(len(nodes)):
        node = nodes[i]
        if node is not None:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                node.left = nodes[left_idx]
            if right_idx < len(nodes):
                node.right = nodes[right_idx]
    return nodes[0]

def print_tree(root):
    def depth(node):
        if not node:
            return 0
        return 1 + max(depth(node.left), depth(node.right))
    
    positions = {}
    
    def fill_positions(node, x, y):
        if not node:
            return
        positions[(x, y)] = node.val
        fill_positions(node.left, x + 1, y - 1)
        fill_positions(node.right, x + 1, y + 1)
    
    fill_positions(root, 0, 0)
    
    rows = {}
    for (x, y), val in positions.items():
        rows.setdefault(x, {})[y] = val
    
    all_y = [y for (_, y) in positions.keys()]
    min_y = min(all_y) if all_y else 0
    
    max_depth = depth(root)
    width = max(all_y) - min_y + 1
    grid = [[' ' for _ in range(width * 2)] for __ in range(max_depth * 2)]
    
    for (x, y), val in positions.items():
        col = (y - min_y) * 2
        row = x * 2
        val_str = str(val)
        for i, ch in enumerate(val_str):
            grid[row][col + i] = ch
    
    def draw_line(parent_x, parent_y, child_x, child_y):
        p_row = parent_x * 2
        p_col = (parent_y - min_y) * 2
        c_row = child_x * 2
        c_col = (child_y - min_y) * 2
        
        if child_y < parent_y:
            steps = c_row - p_row
            for step in range(1, steps):
                grid[p_row + step][p_col - step] = '/'
        else:
            steps = c_row - p_row
            for step in range(1, steps):
                grid[p_row + step][p_col + step] = '\\'
    
    def add_links(node, x, y):
        if not node:
            return
        if node.left:
            draw_line(x, y, x + 1, y - 1)
            add_links(node.left, x + 1, y - 1)
        if node.right:
            draw_line(x, y, x + 1, y + 1)
            add_links(node.right, x + 1, y + 1)
    
    add_links(root, 0, 0)
    
    non_empty_rows = [i for i, row in enumerate(grid) if any(ch != ' ' for ch in row)]
    if not non_empty_rows:
        return
    start_row = non_empty_rows[0]
    end_row = non_empty_rows[-1] + 1
    
    for i in range(start_row, end_row):
        line = ''.join(grid[i]).rstrip()
        if line:
            print(line)

arr = arr = [10, 5, 15, 2, 7, None, 20, 1, None, 6, 8]
root = build_tree_from_array(arr)
print_tree(root)