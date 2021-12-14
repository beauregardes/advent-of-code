import numpy as np
import time


class OceanFloor:
    def __init__(self, max_row, max_col):
        rows = max(max_row[0][1], max_row[1][1])
        cols = max(max_col[0][0], max_col[1][0])
        self.grid = np.zeros((rows+1, cols+1))

    def mark(self, p1, p2):
        self.bresenham(p1[0], p1[1], p2[0], p2[1])

    def bresenham(self, x0, y0, x1, y1):
        def plot_line_low(x0, y0, x1, y1):
            dx, dy, yi = x1 - x0, y1 - y0, 1
            if dy < 0:
                yi, dy = -1, -dy
            d, y = (2 * dy) - dx, y0
            for x in range(x0, x1 + 1):
                self.grid[y, x] += 1
                if d > 0:
                    y, d = y + yi, d + (2 * (dy - dx))
                else:
                    d += 2 * dy

        def plot_line_high(x0, y0, x1, y1):
            dx, dy, xi = x1 - x0, y1 - y0, 1
            if dx < 0:
                xi, dx = -1, -dx
            d, x = (2 * dx) - dy, x0
            for y in range(y0, y1 + 1):
                self.grid[y, x] += 1
                if d > 0:
                    x, d = x + xi, d + (2 * (dx - dy))
                else:
                    d += 2 * dx

        if abs(y1 - y0) < abs(x1 - x0):
            if x0 > x1:
                plot_line_low(x1, y1, x0, y0)
            else:
                plot_line_low(x0, y0, x1, y1)
        else:
            if y0 > y1:
                plot_line_high(x1, y1, x0, y0)
            else:
                plot_line_high(x0, y0, x1, y1)

    def count_gte_n(self, n):
        return np.sum(self.grid >= n)


def main():
    with open('2021/input/5.txt', 'r') as f:
        raw = map(lambda l: l.strip(), f.readlines())

    def get_point(l):
        p1_raw, p2_raw = l.split(' -> ')
        p1_x, p1_y = p1_raw.split(',')
        p2_x, p2_y = p2_raw.split(',')
        return [
            (int(p1_x), int(p1_y)),
            (int(p2_x), int(p2_y))
        ]
    lines = [get_point(l) for l in raw]
    max_row = max(lines, key=lambda l: max(l[0][1], l[1][1]))
    max_col = max(lines, key=lambda l: max(l[0][0], l[1][0]))

    p1_ocean = OceanFloor(max_row, max_col)
    p2_ocean = OceanFloor(max_row, max_col)
    for l in lines:
        if l[0][0] == l[1][0] or l[0][1] == l[1][1]:
            p1_ocean.mark(l[0], l[1])
        p2_ocean.mark(l[0], l[1])

    return p1_ocean.count_gte_n(2), p2_ocean.count_gte_n(2)


if __name__ == '__main__':
    t1 = time.time()
    p1_ans, p2_ans = main()
    t2 = time.time()

    print(f"P1: {p1_ans}")  # => 6461
    print(f"P2: {p2_ans}")  # => 18065
    print(f"Took {t2 - t1}s")
