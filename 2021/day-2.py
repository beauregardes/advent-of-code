import time


def main():
    p1_pos, p2_pos = [0, 0], [0, 0, 0]

    with open('2021/input/2.txt', 'r') as f:
        movements = f.readlines()

    # P1
    for move in movements:
        direction, units = move.split(' ')
        if direction == "forward":
            p1_pos[0] += int(units)
        elif direction == "down":
            p1_pos[1] += int(units)
        elif direction == "up":
            p1_pos[1] -= int(units)

    # P2
    for move in movements:
        direction, units = move.split(' ')
        if direction == "forward":
            p2_pos[0] += int(units)
            p2_pos[1] += p2_pos[2] * int(units)
        elif direction == "down":
            p2_pos[2] += int(units)
        elif direction == "up":
            p2_pos[2] -= int(units)

    return p1_pos[0] * p1_pos[1], p2_pos[0] * p2_pos[1]


if __name__ == '__main__':
    t1 = time.time()
    p1_ans, p2_ans = main()
    t2 = time.time()

    print(f"P1: {p1_ans}")  # => 1728414
    print(f"P2: {p2_ans}")  # => 1765720035

    print(f"Took {t2 - t1}s")
