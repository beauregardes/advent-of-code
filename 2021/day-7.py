import time


def sum_1_to_n(n):
    return (n * (n + 1)) // 2


def main():
    with open('2021/input/7.txt', 'r') as f:
        positions = list(map(int, f.read().strip().split(',')))

    min_p = min(positions)
    max_p = max(positions)

    p1_ans = min(
        [sum(abs(p - i) for p in positions)
         for i in range(min_p, max_p + 1)]
    )

    p2_ans = min(
        [sum(sum_1_to_n(abs(p - i)) for p in positions)
         for i in range(min_p, max_p + 1)]
    )

    return p1_ans, p2_ans


if __name__ == '__main__':
    t1 = time.time()
    p1_ans, p2_ans = main()
    t2 = time.time()

    print(f"P1: {p1_ans}")  # => 351901
    print(f"P2: {p2_ans}")  # => 101079875

    print(f"Took {t2 - t1}s")
