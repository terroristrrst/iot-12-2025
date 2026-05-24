class MaxFlowSolver:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.capacity = []
        for i in range(num_nodes):
            self.capacity.append([0] * num_nodes)

    def add_edge(self, u, v, cap): # u звідки виїзджають, v куди їдуть, cap - кількість машин, які можуть проїхати по цьому шляху
        self.capacity[u][v] += cap

    def bfs_path(self, parent, source, sink):
        visited = [False] * self.num_nodes
        queue = [source]
        visited[source] = True
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for v in range(self.num_nodes):
                if not visited[v] and self.capacity[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
                    queue.append(v)
        return False

    def max_flow(self, source, sink):
        parent = [-1] * self.num_nodes
        total_flow = 0
        while self.bfs_path(parent, source, sink):
            path_flow = float('inf')
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.capacity[u][v])
                v = u
            v = sink
            while v != source:
                u = parent[v]
                self.capacity[u][v] -= path_flow
                self.capacity[v][u] += path_flow
                v = u
            total_flow += path_flow
        return total_flow

def read_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    if len(lines) < 2:
        return None, None, None
    farms = [x.strip() for x in lines[0].split(',')]
    shops = [x.strip() for x in lines[1].split(',')]
    edges = []
    for line in lines[2:]:
        parts = [x.strip() for x in line.split(',')]
        if len(parts) == 3:
            u, v, cap = parts[0], parts[1], int(parts[2])
            edges.append((u, v, cap))
    return farms, shops, edges

def main():
    farms, shops, edges = read_input('roads.csv')
    if farms is None:
        print(0)
        return
    nodes = set()
    for f in farms:
        nodes.add(f)
    for s in shops:
        nodes.add(s)
    for u, v, _ in edges:
        nodes.add(u)
        nodes.add(v)
    node_list = list(nodes)
    node_index = {name: i for i, name in enumerate(node_list)}
    n = len(node_list)
    source = n
    sink = n + 1
    solver = MaxFlowSolver(n + 2)
    INF = 10**9
    for f in farms:
        solver.add_edge(source, node_index[f], INF)
    for s in shops:
        solver.add_edge(node_index[s], sink, INF)
    for u, v, cap in edges:
        iu = node_index[u]
        iv = node_index[v]
        solver.add_edge(iu, iv, cap)
        solver.add_edge(iv, iu, cap)
    result = solver.max_flow(source, sink)
    print(result)

if __name__ == '__main__':
    main()