import heapq as hq
import time
import pprint

class Graph:
    def __init__(self):
        self.adj = {}

    def set_weight(self, src, dst, v):
        if src not in self.adj:
            self.adj[src] = {}
        self.adj[src][dst] = v

    def get_weight(self, src, dst):
        return self.adj[src][dst]

    def get_neighbors(self, src):
        return self.adj[src].keys()

    def dijkstra(self, src, dst):
        dist, prev = {}, {}

        dist[src] = 0
        for v in self.adj.keys():
            if v != src:
                dist[v] = float('inf')
            prev[v] = None

        Q = []
        hq.heappush(Q, (float('inf'), src))
        
        seen = set()
        while len(Q) > 0:
            u = hq.heappop(Q)[1]
            if u == dst:
                break

            # We have already processed this node with 
            # a lower priority, so we skip it now
            if u in seen:
                continue
            seen.add(u)
            
            for v in self.get_neighbors(u):
                alt = dist[u] + self.get_weight(u, v)
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    hq.heappush(Q, (alt, v))

        S = []
        u = dst
        while u is not None:
            S.append(u)
            u = prev[u]
        S.reverse()

        return S


def graph_from_risk_levels(risk_levels):
    rows = len(risk_levels)
    cols = len(risk_levels[0])
    def rl(i):
        return risk_levels[i // cols][i % cols]

    g = Graph()
    for i in range(rows * cols):
        if i // cols > 0:  # N
            g.set_weight(i, i - cols, rl(i - cols))
        if i // cols < rows - 1:  # S
            g.set_weight(i, i + cols, rl(i + cols))
        if i % cols != 0:  # W
            g.set_weight(i, i - 1, rl(i - 1))
        if (i + 1) % cols != 0:  # E
            g.set_weight(i, i + 1, rl(i + 1))

    return g


def main():
    with open('2021/input/15.txt', 'r') as f:
        risk_levels = list(map(lambda l: list(map(int, list(l.strip()))), f.readlines()))

    g1 = graph_from_risk_levels(risk_levels)
    path = g1.dijkstra(0, (len(risk_levels) * len(risk_levels[0])) - 1)

    p1_ans = 0
    for i in range(len(path) - 1):
        p1_ans += g1.get_weight(path[i], path[i + 1])

    risk_levels_extended = [[] for _ in range(len(risk_levels) * 5)]
    for y in range(5):
        for x in range(5):
            for ry in range(len(risk_levels)):
                for rx in range(len(risk_levels[ry])):
                    rl = (risk_levels[ry][rx] + x + y) % 10
                    if rl < risk_levels[ry][rx]:
                        rl += 1
                    rley = (y * len(risk_levels)) + ry
                    risk_levels_extended[rley].append(rl)

    g2 = graph_from_risk_levels(risk_levels_extended)
    path = g2.dijkstra(0, (len(risk_levels_extended) * len(risk_levels_extended[0])) - 1)

    p2_ans = 0
    for i in range(len(path) - 1):
        p2_ans += g2.get_weight(path[i], path[i + 1])

    return p1_ans, p2_ans


if __name__ == '__main__':
    t1 = time.time()
    p1_ans, p2_ans = main()
    t2 = time.time()

    print(f"P1: {p1_ans}")  # => 537
    print(f"P2: {p2_ans}")  # => 2881

    print(f"Took {t2 - t1}s")
