class MaxFlowSolver:
    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes
        self.capacity = [[0] * num_nodes for _ in range(num_nodes)]

    def add_edge(self, u: int, v: int, cap: int) -> None:
        self.capacity[u][v] += cap

    def bfs(self, parent: list, source: int, sink: int) -> bool:
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

    def max_flow(self, source: int, sink: int) -> int:
        parent = [-1] * self.num_nodes
        total_flow = 0
        while self.bfs(parent, source, sink):
            path_flow = float("inf")
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


def parse_csv_content(lines: list) -> tuple:
    if len(lines) < 2:
        return [], [], []
    farms = [x.strip() for x in lines[0].split(",")]
    shops = [x.strip() for x in lines[1].split(",")]
    edges = []
    for line in lines[2:]:
        if not line.strip():
            continue
        parts = [x.strip() for x in line.split(",")]
        if len(parts) == 3:
            u, v, cap = parts[0], parts[1], int(parts[2])
            edges.append((u, v, cap))
    return farms, shops, edges


def build_network(farms, shops, edges):
    nodes = set(farms) | set(shops)
    for u, v, _ in edges:
        nodes.add(u)
        nodes.add(v)
    node_list = list(nodes)
    node_index = {name: idx for idx, name in enumerate(node_list)}
    n = len(node_list)
    source = n
    sink = n + 1
    solver = MaxFlowSolver(n + 2)
    INF = 10 ** 9
    for farm in farms:
        solver.add_edge(source, node_index[farm], INF)
    for shop in shops:
        solver.add_edge(node_index[shop], sink, INF)
    for u, v, cap in edges:
        iu = node_index[u]
        iv = node_index[v]
        solver.add_edge(iu, iv, cap)
        solver.add_edge(iv, iu, cap)
    return solver, source, sink


def compute_max_flow_from_file(filename: str) -> int:
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    farms, shops, edges = parse_csv_content(lines)
    if not farms or not shops:
        return 0
    solver, source, sink = build_network(farms, shops, edges)
    return solver.max_flow(source, sink)