import time


class Graph:
    class Cave:
        def __init__(self, name):
            self.name = name
            self.cxxns = []

        def add_cxxn(self, c):
            self.cxxns.append(c)

        def get_available_cxxns_p1(self, small_visited):
            return list(filter(lambda c: c.name not in small_visited, self.cxxns))

        def get_available_cxxns_p2(self, small_twiced, small_visited):
            if small_twiced:
                return list(filter(lambda c: c.name not in small_visited, self.cxxns))
            else:
                return list(filter(lambda c: c.name != "start", self.cxxns))

    def __init__(self):
        self.caves = {}

    def add_cxxn(self, src, dst):
        if src not in self.caves:
            self.caves[src] = self.Cave(src)
        if dst not in self.caves:
            self.caves[dst] = self.Cave(dst)
        self.caves[src].add_cxxn(self.caves[dst])
        self.caves[dst].add_cxxn(self.caves[src])

    def get_cave(self, c):
        return self.caves[c]


def spelunk_all_caves_p1(g, curr, small_visited):
    if curr.name == 'end':
        return 1

    if curr.name.islower():
        small_visited.add(curr.name)

    n = 0
    available_cxxns = curr.get_available_cxxns_p1(small_visited)
    for c in available_cxxns:
        n += spelunk_all_caves_p1(g, c, small_visited.copy())
    return n


def spelunk_all_caves_p2(g, curr, small_twiced, small_visited):
    if curr.name == 'end':
        return 1

    if not small_twiced and curr.name.islower() and curr.name in small_visited:
        small_twiced = True
    
    if curr.name.islower():
        small_visited.add(curr.name)

    n = 0
    available_cxxns = curr.get_available_cxxns_p2(small_twiced, small_visited)
    for c in available_cxxns:
        n += spelunk_all_caves_p2(g, c, small_twiced, small_visited.copy())
    return n


def main():
    with open('2021/input/12.txt', 'r') as f:
        graph_defs = list(map(lambda l: l.strip(), f.readlines()))

    g = Graph()
    for d in graph_defs:
        src, dst = d.split('-')
        g.add_cxxn(src, dst)

    p1_ans = spelunk_all_caves_p1(g, g.get_cave('start'), set())
    p2_ans = spelunk_all_caves_p2(g, g.get_cave('start'), False, set())

    return p1_ans, p2_ans


if __name__ == '__main__':
    t1 = time.time()
    p1_ans, p2_ans = main()
    t2 = time.time()

    print(f"P1: {p1_ans}")  # =>
    print(f"P2: {p2_ans}")  # =>

    print(f"Took {t2 - t1}s")
