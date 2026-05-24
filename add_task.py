import os
import json

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def load_tree_from_config(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    with open(file_path, 'r') as f:
        data = json.load(f)

    node_values = data.get("nodes", {})
    root_val = data.get("root")

    nodes = {int(v): BinaryTree(int(v)) for v in node_values.keys()}
    all_referenced = set()
    for v in node_values.values():
        if v.get("left"): all_referenced.add(v["left"])
        if v.get("right"): all_referenced.add(v["right"])
    
    for val in all_referenced.union({root_val}):
        if val not in nodes:
            nodes[val] = BinaryTree(val)

    for val, children in node_values.items():
        current_node = nodes[int(val)]
        if "left" in children:
            current_node.left = nodes[children["left"]]
        if "right" in children:
            current_node.right = nodes[children["right"]]

    return nodes.get(root_val)

def render_top_view(tree):
    width, height = 120, 40
    grid = [[" " for _ in range(width)] for _ in range(height)]

    def write(x, y, text):
        if 0 <= y < height:
            s = str(text)
            for i, c in enumerate(s):
                if 0 <= x + i < width:
                    grid[y][x + i] = c

    cx, cy = 60, 20
    if not tree:
        return
    
    write(cx, cy, tree.value)

    def draw_math_top(node, x, y, dx_sign, y_step):
        dx = 10 * dx_sign
        if node.left:
            nx, ny = x + dx, y + y_step
            char = "/" if dx_sign < 0 else "\\"
            write(x + dx//2, y + y_step//2, char)
            write(nx, ny, node.left.value)
            draw_math_top(node.left, nx, ny, dx_sign, max(2, y_step - 1))
        if node.right:
            nx, ny = x + dx, y - y_step
            char = "\\" if dx_sign < 0 else "/"
            write(x + dx//2, y - y_step//2, char)
            write(nx, ny, node.right.value)
            draw_math_top(node.right, nx, ny, dx_sign, max(2, y_step - 1))

    if tree.left:
        for i in range(cx - 6, cx):
            grid[cy][i] = "-"
        write(cx - 8, cy, tree.left.value)
        draw_math_top(tree.left, cx - 8, cy, -1, 6)

    if tree.right:
        for i in range(cx + 2, cx + 8):
            grid[cy][i] = "-"
        write(cx + 9, cy, tree.right.value)
        draw_math_top(tree.right, cx + 9, cy, 1, 6)

    for row in grid:
        line = "".join(row).rstrip()
        if line:
            print(line)

if __name__ == "__main__":
    config_path = "config.json"
    tree = load_tree_from_config(config_path)
    
    if tree:
        print("Top View of the Binary Tree:\n")
        render_top_view(tree)