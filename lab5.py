def find_min_depth(root, graph):
    if root is None:
        return 0

    queue = [(root, 1)]
    head = 0

    while head < len(queue):
        node, depth = queue[head]
        head += 1

        children = graph.get(node, [])
        if not children:
            return depth

        for child in children:
            queue.append((child, depth + 1))

    return 1


with open('input.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

if not lines:
    min_depth = 0
else:
    root = int(lines[0])
    graph = {}

    for line in lines[1:]:
        if ',' not in line:
            continue
        parent_str, child_str = line.split(',')
        parent = int(parent_str)
        child = int(child_str)
        if parent not in graph:
            graph[parent] = []
        graph[parent].append(child)

    min_depth = find_min_depth(root, graph)

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(str(min_depth))