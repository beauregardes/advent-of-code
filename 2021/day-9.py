import time
import math


def main():
    offsets = [[-1, 0], [1, -1], [0, -1], [0, 1]]

    with open('2021/input/9.txt', 'r') as f:
        heightmap = list(map(lambda l: list(map(int, list(l.strip()))), f.readlines()))
    # pad the top and bottom
    heightmap_w = len(heightmap[0])
    heightmap = [
      ([9] * (heightmap_w + 2)),
      *heightmap,
      ([9] * (heightmap_w + 2))
    ]

    p1_ans = 0

    low_points = []
    basin_sizes = []

    for r in range(1, len(heightmap) - 1):
        heightmap[r] = [9, *heightmap[r], 9]
        c = 1
        while c < len(heightmap[r]) - 1:
            if heightmap[r][c] < 9:
                if all(map(lambda o: heightmap[r + o[0]][c + o[1]] > heightmap[r][c], offsets)):
                    p1_ans += heightmap[r][c] + 1
                    low_points.append((r, c))
                    c += 1  # skip the next one, it can't possibly be a low point
            c += 1

    def flood_fill_basin(visited, r, c):
        if visited[r][c]:
            return 0
        visited[r][c] = True

        if heightmap[r][c] == 9:
            return 0
        else:
            return 1 + \
                flood_fill_basin(visited, r + 1, c) + \
                flood_fill_basin(visited, r, c + 1) + \
                flood_fill_basin(visited, r - 1, c) + \
                flood_fill_basin(visited, r, c - 1)

    for lp in low_points:
        visited = [[False for _ in range(len(heightmap[0]))] for _ in range(len(heightmap))]
        basin_sizes.append(flood_fill_basin(visited, lp[0], lp[1]))

    return p1_ans, math.prod(sorted(basin_sizes, reverse=True)[:3])


if __name__ == '__main__':
    t1 = time.time()
    p1_ans, p2_ans = main()
    t2 = time.time()

    print(f"P1: {p1_ans}")  # => 541
    print(f"P2: {p2_ans}")  # => 

    print(f"Took {t2 - t1}s")
